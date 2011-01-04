import unittest
from should_dsl import should
from ludibrio import Stub
from domain.movement import Movement

class MovementSpec(unittest.TestCase):

    def setUp(self):
        self.movement = Movement()

    def simulates_some_movement_performing(self):
        return 'I can perform somehow'

    def it_defines_how_a_movement_performs(self):
        #since nothing was done, process_resources must be an alias for todo()
        self.movement.perform |should| equal_to(self.movement.todo)
        #now it will learn how to perform
        self.movement.define_how_to_perform(self.simulates_some_movement_performing)
        self.movement.perform |should| equal_to(self.simulates_some_movement_performing)

    def it_configures_a_movement(self):
        #a complete configuration
        with Stub() as configuration:
            configuration.mask        >> 'payment'
            configuration.version     >> 'monthly'
            configuration.category    >> 'financial'
            configuration.description >> 'a monthly payment from an organization to a person'
            configuration.allowable_resource_masks_and_versions         >> [['money','dollar'],['money','euro']]
            configuration.allowable_resource_categories                 >> ['financial']
            configuration.allowable_source_node_masks_and_versions      >> [['branch','generic']]
            configuration.allowable_source_node_categories              >> ['person','organization']
            configuration.allowable_destination_node_masks_and_versions >> [['employee','40 hours'],['employee','generic']]
            configuration.allowable_destination_node_categories         >> ['person','organization']
        self.movement.configure(configuration)
        #should be: self.movement.configuration |should| equal_to(self.configuration)
        self.movement.configuration.mask |should| equal_to('payment')
        self.movement.configuration.version |should| equal_to('monthly')

    def it_sets_a_source_node(self):
        #allowable by category
        with Stub() as configuration:
            configuration.mask        >> 'payment'
            configuration.version     >> 'monthly'
            configuration.allowable_source_node_categories >> ['person','organization']
            configuration.allowable_source_node_masks_and_versions >> []
        self.movement.configure(configuration)
        with Stub() as source:
            source.mask     >> 'branch'
            source.version  >> 'generic'
            source.category >> 'organization'
            source.title    >> 'London Branch'
        self.movement.set_source_node(source)
        #should be: self.movement.source_node |should| equal_to(source)
        self.movement.source_node.title |should| equal_to('London Branch')
        #allowable by mask and version
        with Stub() as configuration:
            configuration.mask        >> 'payment'
            configuration.version     >> 'monthly'
            configuration.allowable_source_node_masks_and_versions >> [['branch','generic']]
            configuration.allowable_source_node_categories >> []
        self.movement.configure(configuration)
        self.movement.set_source_node(source)
        #should be: self.movement.source_node |should| equal_to(source)
        self.movement.source_node.title |should| equal_to('London Branch')
        #error
        with Stub() as configuration:
            configuration.mask        >> 'payment'
            configuration.version     >> 'monthly'
            configuration.allowable_source_node_masks_and_versions >> []
            configuration.allowable_source_node_categories >> []
        self.movement.configure(configuration)
        (self.movement.set_source_node, source) |should| throw(ValueError)

    def it_sets_a_destination_node(self):
        #allowable by category
        with Stub() as configuration:
            configuration.mask        >> 'payment'
            configuration.version     >> 'monthly'
            configuration.allowable_destination_node_categories >> ['person','organization']
            configuration.allowable_destination_node_masks_and_versions >> []
        self.movement.configure(configuration)
        with Stub() as destination:
            destination.mask     >> 'employee'
            destination.version  >> '40 hours'
            destination.category >> 'person'
            destination.title    >> 'Bruce Dickson'
        self.movement.set_destination_node(destination)
        #should be: self.movement.source_node |should| equal_to(source)
        self.movement.destination_node.title |should| equal_to('Bruce Dickson')
        #allowable by mask and version
        with Stub() as configuration:
            configuration.mask        >> 'payment'
            configuration.version     >> 'monthly'
            configuration.allowable_destination_node_masks_and_versions >> [['employee','40 hours']]
            configuration.allowable_destination_node_categories >> []
        self.movement.configure(configuration)
        self.movement.set_destination_node(destination)
        #should be: self.movement.source_node |should| equal_to(source)
        self.movement.destination_node.title |should| equal_to('Bruce Dickson')
        #error
        with Stub() as configuration:
            configuration.mask        >> 'payment'
            configuration.version     >> 'monthly'
            configuration.allowable_destination_node_masks_and_versions >> []
            configuration.allowable_destination_node_categories >> []
        self.movement.configure(configuration)
        (self.movement.set_destination_node, destination) |should| throw(ValueError)

    def it_sets_a_resource(self):
        #allowable by category
        with Stub() as configuration:
            configuration.mask        >> 'payment'
            configuration.version     >> 'monthly'
            configuration.allowable_resource_categories >> ['financial']
            configuration.allowable_resource_masks_and_versions >> []
        self.movement.configure(configuration)
        with Stub() as resource:
            resource.mask     >> 'money'
            resource.version  >> 'euro'
            resource.category >> 'financial'
            resource.title    >> 'salary'
        self.movement.set_resource(resource)
        #should be: self.movement.source_node |should| equal_to(source)
        self.movement.resource.title |should| equal_to('salary')
        #allowable by mask and version
        with Stub() as configuration:
            configuration.mask        >> 'payment'
            configuration.version     >> 'monthly'
            configuration.allowable_resource_masks_and_versions >> [['money','euro']]
            configuration.allowable_resource_categories >> []
        self.movement.configure(configuration)
        self.movement.set_resource(resource)
        #should be: self.movement.source_node |should| equal_to(source)
        self.movement.resource.title |should| equal_to('salary')
        #error
        with Stub() as configuration:
            configuration.mask        >> 'payment'
            configuration.version     >> 'monthly'
            configuration.allowable_resource_masks_and_versions >> []
            configuration.allowable_resource_categories >> []
        self.movement.configure(configuration)
        (self.movement.set_resource, resource) |should| throw(ValueError)

