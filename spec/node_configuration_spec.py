import unittest
from ludibrio import Stub
from should_dsl import should
from domain.node_configuration import NodeConfiguration

class NodeConfigurationSpec(unittest.TestCase):

    def setUp(self):
        self.node_configuration = NodeConfiguration()
        #an example configuration
        self.node_configuration.mask        = 'developer'
        self.node_configuration.version     = 'junior 1.0'
        self.node_configuration.category    = 'employee'
        self.node_configuration.description = 'with less than three years of experience'
        self.node_configuration.allowable_resource_masks_and_versions = [['Ruby skill','intermediary'],['Python skill','intermediary']]
        self.node_configuration.allowable_resource_categories         = ['Programming skill']

    def it_checks_a_resource_compatibility(self):
        #allowable by category
        with Stub() as resource:
            resource.configuration.mask     >> 'Python skill'
            resource.configuration.version  >> 'intermediary'
            resource.configuration.category >> 'Programming skill'
        #I have set and clean allowable collections to isolate each condition
        self.node_configuration.allowable_resource_masks_and_versions = []
        self.node_configuration.allowable_resource_categories = ['Programming skill']
        self.node_configuration.check_resource_compatibility(resource) |should| equal_to('Compatible resource configuration')
        #allowable by mask and version
        self.node_configuration.allowable_resource_categories = []
        self.node_configuration.allowable_resource_masks_and_versions = [['Ruby skill','intermediary'],['Python skill','intermediary']]
        self.node_configuration.check_resource_compatibility(resource) |should| equal_to('Compatible resource configuration')
        #error: empty allowables
        self.node_configuration.allowable_resource_masks_and_versions = []
        self.node_configuration.allowable_resource_categories = []
        (self.node_configuration.check_resource_compatibility, resource) |should| throw(ValueError)

    def it_parses_a_node_configuration(self):
        '''I am not parsing a node configuration in fact'''

    def it_persists_a_node_configuration(self):
        '''I am not persisting a node configuration in fact'''

    def it_retrieves_a_node_configuration_from_some_storage(self):
        '''I am not retrieving a node configuration in fact'''

    def it_lists_the_available_configurations_for_a_given_node(self):
        '''I am not listing the available configurations in fact'''

