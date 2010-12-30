import unittest
from should_dsl import should
from domain.resource import Resource
from domain.resource_configuration import ResourceConfiguration

class ResourceConfigurationSpec(unittest.TestCase):

    def setUp(self):
        self.resource_configuration = ResourceConfiguration()

    def it_parses_a_resource_configuration(self):
        '''I am not parsing a resource configuration in fact'''
        self.resource_configuration.read('developer','junior 1.0')
        #should be done by parse/retrieve in fact
        self.resource_configuration.configuration_text = 'A programming is a skill, which represents the capacity of developing programms, measured by development hours'
        self.resource_configuration.configuration_text |should| equal_to('A programming is a skill, which represents the capacity of developing programms, measured by development hours')

    def it_persists_a_resource_configuration(self):
        '''I am not persisting a resource configuration in fact'''

    def it_retrieves_a_resource_configuration_from_some_storage(self):
        '''I am not retrieving a resource configuration in fact'''

    def it_lists_the_available_configurations_for_a_given_resource(self):
        '''I am not listing the available configurations in fact'''

