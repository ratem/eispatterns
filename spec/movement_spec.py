import unittest
from should_dsl import should
from ludibrio import Stub, Mock
from domain.movement import Movement
from domain.movement_configuration import MovementConfiguration

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

    # "Classism" to test relationship between movement and its configurator
    # "Mockism" to test relationship with other concepts
    def it_configures_a_movement(self):
        configuration = MovementConfiguration()
        #a complete configuration
        configuration.mask        = 'payment'
        configuration.version     = 'monthly'
        configuration.category    = 'financial'
        configuration.description = 'a monthly payment from an organization to a person'
        configuration.allowable_resource_masks_and_versions         = [['money','dollar'],['money','euro']]
        configuration.allowable_resource_categories                 = ['financial']
        configuration.allowable_source_node_masks_and_versions      = [['branch','generic']]
        configuration.allowable_source_node_categories              = ['person','organization']
        configuration.allowable_destination_node_masks_and_versions = [['employee','40 hours'],['employee','generic']]
        configuration.allowable_destination_node_categories         = ['person','organization']
        self.movement.configure(configuration)
        self.movement.configuration |should| equal_to(configuration)
        #a non compatible configuration
        with Stub() as configuration_stub:
            configuration_stub.mask >> 'My class is invalid for configurating'
        (self.movement.configure, configuration_stub) |should| throw(KeyError)

    # "Exaustive" tests are done in movement_configuration_spec, here tests only
    # how compatibible and non-compatible are treated by Movement
    def it_sets_a_resource(self):
        configuration = MovementConfiguration()
        configuration.allowable_resource_categories = ['financial']
        self.movement.configure(configuration)
        #compatible somehow
        with Stub() as resource:
            resource.configuration.category >> 'financial'
        self.movement.set_resource(resource)
            #self.movement.resource |should| equal_to(resource)
        self.movement.resource.category |should| equal_to('financial')
        #non compatible somehow
        with Stub() as resource:
            resource.configuration.category >> 'human skill'
        (self.movement.set_resource, resource) |should| throw(ValueError)

    def it_sets_a_source_node(self):
        configuration = MovementConfiguration()
        configuration.allowable_source_node_categories = ['person','organization']
        self.movement.configure(configuration)
        #compatible somehow
        with Stub() as source_node:
            source_node.configuration.category >> 'organization'
        self.movement.set_source_node(source_node)
            #self.movement.source_node |should| equal_to(source_node)
        self.movement.source_node.category |should| equal_to('organization')
        #non compatible somehow
        with Stub() as source_node:
            source_node.configuration.category >> 'manufacturing cell'
        (self.movement.set_source_node, source_node) |should| throw(ValueError)

    def it_sets_a_destination_node(self):
        configuration = MovementConfiguration()
        configuration.allowable_destination_node_categories = ['person','organization']
        self.movement.configure(configuration)
        #compatible somehow
        with Stub() as destination_node:
            destination_node.configuration.category >> 'person'
        self.movement.set_destination_node(destination_node)
            #self.movement.destination_node |should| equal_to(destination_node)
        self.movement.destination_node.category |should| equal_to('person')
        #non compatible somehow
        with Stub() as destination_node:
            destination_node.configuration.category >> 'cnc'
        (self.movement.set_destination_node, destination_node) |should| throw(ValueError)

