import unittest
from should_dsl import should
from ludibrio import Stub
from domain.resource.resource import Resource

class ResourceSpec(unittest.TestCase):

    def setUp(self):
        self.resource = Resource()

