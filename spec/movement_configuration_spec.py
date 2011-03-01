import unittest
from should_dsl import should
from ludibrio import Stub
from domain.movement_configuration import MovementConfiguration

class MovementConfigurationSpec(unittest.TestCase):

    def setUp(self):
        self.movement_configuration = MovementConfiguration()
        #a complete configuration example
        self.movement_configuration.mask        = 'payment'
        self.movement_configuration.version     = 'monthly'
        self.movement_configuration.category    = 'financial'
        self.movement_configuration.description = 'a monthly payment from an organization to a person'
        self.movement_configuration.allowable_resource_masks_and_versions         = [['money','dollar'],['money','euro']]
        self.movement_configuration.allowable_resource_categories                 = ['financial']
        self.movement_configuration.allowable_source_node_masks_and_versions      = [['branch','generic'],['person','generic']]
        self.movement_configuration.allowable_source_node_categories              = ['person','organization']
        self.movement_configuration.allowable_destination_node_masks_and_versions = [['employee','40 hours'],['employee','generic']]
        self.movement_configuration.allowable_destination_node_categories         = ['person','organization']

    def it_checks_a_resource_compatibility(self):
        #allowable by category
        with Stub() as resource:
            resource.configuration.mask     >> 'money'
            resource.configuration.version  >> 'euro'
            resource.configuration.category >> 'financial'
            resource.configuration.title    >> 'salary'
        self.movement_configuration.allowable_resource_masks_and_versions = []
        self.movement_configuration.allowable_resource_categories = ['financial']
        self.movement_configuration.check_resource_compatibility(resource) |should| equal_to('Compatible resource configuration')
        #allowable by mask and version
        self.movement_configuration.allowable_resource_categories = []
        self.movement_configuration.allowable_resource_masks_and_versions = [['money','dollar'],['money','euro']]
        self.movement_configuration.check_resource_compatibility(resource) |should| equal_to('Compatible resource configuration')
        #error: empty allowables
        self.movement_configuration.allowable_resource_masks_and_versions = []
        self.movement_configuration.allowable_resource_categories = []
        (self.movement_configuration.check_resource_compatibility, resource) |should| throw(ValueError)

    def it_checks_a_source_node_compatibility(self):
        #allowable by category
        with Stub() as source:
            source.configuration.mask     >> 'branch'
            source.configuration.version  >> 'generic'
            source.configuration.category >> 'organization'
            source.configuration.title    >> 'London Branch'
        self.movement_configuration.allowable_source_node_masks_and_versions = []
        self.movement_configuration.allowable_source_node_categories = ['person','organization']
        self.movement_configuration.check_source_node_compatibility(source) |should| equal_to('Compatible source node configuration')
        #allowable by mask and version
        self.movement_configuration.allowable_source_node_categories = []
        self.movement_configuration.allowable_source_node_masks_and_versions = [['branch','generic'],['person','generic']]
        self.movement_configuration.check_source_node_compatibility(source) |should| equal_to('Compatible source node configuration')
        #error: empty source node configuration
        self.movement_configuration.allowable_source_node_masks_and_versions = []
        self.movement_configuration.allowable_source_node_categories = []
        (self.movement_configuration.check_source_node_compatibility, source) |should| throw(ValueError)

    def it_checks_a_destination_node_compatibility(self):
        #allowable by category
        with Stub() as destination:
            destination.configuration.mask     >> 'employee'
            destination.configuration.version  >> '40 hours'
            destination.configuration.category >> 'person'
            destination.configuration.title    >> 'Bruce Dickson'
        self.movement_configuration.allowable_destination_node_masks_and_versions = []
        self.movement_configuration.allowable_destination_node_categories = ['person','organization']
        self.movement_configuration.check_destination_node_compatibility(destination) |should| equal_to('Compatible destination node configuration')
        #allowable by mask and version
        self.movement_configuration.allowable_destination_node_categories = []
        self.movement_configuration.allowable_destination_node_masks_and_versions = [['employee','40 hours'],['employee','generic']]
        self.movement_configuration.check_destination_node_compatibility(destination) |should| equal_to('Compatible destination node configuration')
        #error: empty destination node configuration
        self.movement_configuration.allowable_destination_node_masks_and_versions = []
        self.movement_configuration.allowable_destination_node_categories = []
        (self.movement_configuration.check_destination_node_compatibility, destination) |should| throw(ValueError)

    def it_parses_a_movement_configuration(self):
        '''I am not parsing a movement configuration in fact'''

    def it_persists_a_movement_configuration(self):
        '''I am not persisting a movement configuration in fact'''

    def it_retrieves_a_movement_configuration_from_some_storage(self):
        '''I am not retrieving a resource configuration in fact'''

    def it_lists_the_available_configurations_for_a_given_movement(self):
        '''I am not listing the available configurations in fact'''

