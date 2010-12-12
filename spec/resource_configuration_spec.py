import unittest
from should_dsl import should
from domain.resource import Resource

class ResourceSpec(unittest.TestCase):

    def setUp(self):
        self.resource = Resource()

    def it_defines_a_use_for_a_resource(self):
        self.resource.define_use()

