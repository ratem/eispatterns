import unittest
from should_dsl import should
from ludibrio import Stub
from domain.resource import Resource
from domain.resource_configuration import ResourceConfiguration

class ResourceConfigurationSpec(unittest.TestCase):

    def it_defines_a_use_for_a_resource(self):
        #defines a callable for implementing 'use', even in runtime
        pass

    def it_obtains_a_configuration(self):
        #Stubs configuration.retrieve(mask, version)
        with Stub() as ResourceConfiguration:
            configuration = ResourceConfiguration()
            configuration.mask >> 'developer'
            configuration.version >>'junior 1.0'
            configuration.type >> 'person'
            configuration.description >> 'someone...'
            configuration.unit >> 'working hours'
        resource = Resource()
        resource.configure(configuration)
        resource.__dict__ |should| equal_to({'use': None, 'tag': None, 'mask': 'developer', 'version' : 'junior 1.0', 'type': 'person', 'description': 'someone...', 'unit':'working hours'})

