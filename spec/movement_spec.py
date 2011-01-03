import unittest
from should_dsl import should
from ludibrio import Stub
from domain.movement import Movement

class MovementSpec(unittest.TestCase):

    def setUp(self):
        self.movement = Movement()
        #will need to set a configuration object many times
        with Stub() as self.configuration:
            self.configuration.mask        >> 'payment'
            self.configuration.version     >> 'monthly'
            self.configuration.category    >> 'financial'
            self.configuration.description >> 'a monthly payment from an organization to a person'
            self.configuration.allowable_resource_masks_and_versions         >> {}
            self.configuration.allowable_resource_categories                 >> ['financial']
            self.configuration.allowable_source_node_masks_and_versions      >> {}
            self.configuration.allowable_source_node_categories              >> ['person','organization']
            self.configuration.allowable_destination_node_masks_and_versions >> {}
            self.configuration.allowable_destination_node_categories         >> ['person','organization']
            #side note: maybe we will have to use hierarchies of categories, such as
            #person->employee/individual_customer
            #organization->holding/branch/organization_customer/government
            #by doing this I can use super-categories to include all subcategories

    def simulates_some_movement_performing(self):
        return 'I can perform somehow'

    def it_configures_a_movement(self):
        self.movement.configure(self.configuration)
        #self.movement.configuration |should| equal_to(self.configuration)
        self.movement.configuration.mask |should| equal_to('payment')
        self.movement.configuration.version |should| equal_to('monthly')

    def it_defines_how_a_movement_performs(self):
        #since nothing was done, process_resources must be an alias for todo()
        self.movement.perform |should| equal_to(self.movement.todo)
        #now it will learn how to perform
        self.movement.define_how_to_perform(self.simulates_some_movement_performing)
        self.movement.perform |should| equal_to(self.simulates_some_movement_performing)

    def it_sets_a_source_node(self):
        #I have to call configure again...
        self.movement.configure(self.configuration)
        with Stub() as source:
            source.mask     >> 'Branch'
            source.version  >> 'generic'
            source.category >> 'organization'
            source.title    >> 'London Branch'
        self.movement.set_source_node(source)
        #self.movement.source_node |should| equal_to(source)
        self.movement.source_node.title |should| equal_to('London Branch')

    def it_sets_a_destination_node(self):
        #I have to call configure again...
        self.movement.configure(self.configuration)
        with Stub() as destination:
            destination.mask     >> 'Employee'
            destination.version  >> 'Singer'
            destination.category >> 'person'
            destination.title    >> 'Bruce Dickson'
        self.movement.set_destination_node(destination)
        #self.movement.destination_node |should| equal_to(destination)
        self.movement.destination_node.title |should| equal_to('Bruce Dickson')

    def it_sets_a_resource(self):
        #I have to call configure again...
        self.movement.configure(self.configuration)
        with Stub() as resource:
            resource.mask     >> 'money'
            resource.version  >> 'euro'
            resource.category >> 'financial'
            resource.title    >> 'use this title to check'
        self.movement.set_resource(resource)
        #self.movement.resource |should| equal_to(resource)
        self.movement.resource.title |should| equal_to('use this title to check')

