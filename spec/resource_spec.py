import unittest
from should_dsl import should
from ludibrio import Stub
from domain.resource import Resource
from domain.resource_configuration import ResourceConfiguration

class ResourceConfigurationSpec(unittest.TestCase):

    def it_defines_a_use_for_a_resource(self):
        #defines a callable for implementing 'use', in the future this can be
        #done in runtime
        pass

