import unittest
from should_dsl import should
from ludibrio import Stub
from domain.resource import Resource

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
        #Stubs a configuration object
        with Stub() as configuration:
            configuration.mask >> 'programming'
            configuration.version >> 'Python'
            configuration.type >> 'skill'
            configuration.description >> 'which represents the capacity of developing programms'
            configuration.unit >> 'development hours'
        #expected_configuration_attributes is defined only in subclasses, forced below
        self.resource.expected_configuration_attributes = ['mask','version','type','description','unit']
        self.resource.configure(configuration)
        self.resource.configuration.mask |should| equal_to('programming')
        self.resource.configuration.version |should| equal_to('Python')
        self.resource.configuration.type |should| equal_to('skill')
        self.resource.configuration.description |should| equal_to('which represents the capacity of developing programms')
        self.resource.configuration.unit |should| equal_to('development hours')

