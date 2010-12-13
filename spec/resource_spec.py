import unittest
from should_dsl import should
from ludibrio import Stub
from domain.resource import Resource
from domain.resource_configuration import ResourceConfiguration

class ResourceConfigurationSpec(unittest.TestCase):

    def it_defines_a_use_for_a_resource(self):
        #defines a callable for implementing 'use', in the future this can be
        #done even in runtime
        pass

    def it_obtains_a_configuration(self):
        #fake double
        configuration = ResourceConfiguration()
        configuration.mask = 'developer'
        configuration.version = 'junior 1.0'
        configuration.type = 'person'
        configuration.description = 'someone...'
        configuration.unit = 'working hours'
        #ok
        resource = Resource()
        resource.configure('developer','junior 1.0')
        #fake attribute setting
        resource.mask = configuration.mask
        resource.version = configuration.version
        resource.type = configuration.type
        resource.description = configuration.description
        resource.unit = configuration.unit

