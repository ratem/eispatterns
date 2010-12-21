import unittest
from should_dsl import should
from domain.resource import Resource
from domain.resource_configuration import ResourceConfiguration

class ResourceConfigurationSpec(unittest.TestCase):

    def setUp(self):
        self.resource_configuration = ResourceConfiguration()

    def it_parses_a_resource_configuration(self):
        self.resource_configuration.read('developer','junior 1.0')
        #should be done by retrieve in fact
        self.resource_configuration.configuration_text = 'A developer is a person, someone able of developing computer programms, measured by working hours'
        self.resource_configuration.configuration_text |should| equal_to('A developer is a person, someone able of developing computer programms, measured by working hours')

    def it_persists_a_resource_configuration(self):
        pass

    def it_retrieves_from_some_storage(self):
        pass

    def it_configures_a_resource(self):
        pass

    def it_lists_the_available_configurations_of_a_given_resource(self):
        pass

