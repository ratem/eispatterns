import unittest
from should_dsl import should
from ludibrio import Stub
from domain.resource import Resource

class ResourceSpec(unittest.TestCase):

    def it_defines_a_use_for_a_resource(self):
        #defines a callable for implementing 'use', even in runtime
        pass

    def it_obtains_a_configuration(self):
        #Stubs a configuration object
        with Stub() as configuration:
            configuration.mask >> 'developer'
            configuration.version >>'junior 1.0'
            configuration.type >> 'person'
            configuration.description >> 'someone...'
            configuration.unit >> 'working hours'
        resource = Resource()
        resource.configure(configuration)
        resource.configuration.mask |should| equal_to('developer')
#        resource.configuration |should| equal_to(configuration)

