import unittest
from should_dsl import should
from ludibrio import Stub
from domain.resource import Resource
from domain.resource_configuration import ResourceConfiguration

class ResourceSpec(unittest.TestCase):

    def setUp(self):
        self.resource = Resource()

    def simulates_some_use_for_a_resource(self):
        return 'I am able to be used'

    def it_defines_a_use_for_a_resource(self):
        #since nothing was done, use must be an alias for todo()
        self.resource.use |should| equal_to(self.resource.todo)
        #now it will learn how to be used
        self.resource.define_how_to_be_used(self.simulates_some_use_for_a_resource)
        self.resource.use |should| equal_to(self.simulates_some_use_for_a_resource)

    def it_configures_a_resource(self):
        #a complete configuration
        configuration = ResourceConfiguration()
        configuration.mask = 'programming'
        configuration.version = 'Python'
        configuration.category = 'skill'
        configuration.description = 'which represents the capacity of developing programms'
        configuration.unit = 'development hours'
        self.resource.configure(configuration)
        self.resource.configuration |should| equal_to(configuration)

