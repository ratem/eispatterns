import unittest
from should_dsl import should
from domain.node_configuration import NodeConfiguration

class NodeConfigurationSpec(unittest.TestCase):

    def setUp(self):
        self.node_configuration = NodeConfiguration()

    def it_parses_a_node_configuration(self):
        '''I am not parsing a node configuration in fact'''
        self.node_configuration.read('developer','junior 1.0')
        #should be done by parse/retrieve in fact
        self.node_configuration.configuration_text = 'A developer version junior 1.0 is a person, with less than three years of experience, able of developing computer programs'
        self.node_configuration.configuration_text |should| equal_to('A developer version junior 1.0 is a person, with less than three years of experience, able of developing computer programs')

    def it_persists_a_node_configuration(self):
        '''I am not persisting a node configuration in fact'''

    def it_retrieves_a_node_configuration_from_some_storage(self):
        '''I am not retrieving a node configuration in fact'''

    def it_lists_the_available_configurations_for_a_given_node(self):
        '''I am not listing the available configurations in fact'''

