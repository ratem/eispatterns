import unittest
from should_dsl import should
from domain.resource import Resource

class ResourceSpec(unittest.TestCase):

    def setUp(self):
        self.resource = Resource()

    def it_maps_a_given_concrete_concept_to_its_mask(self):
        self.resource.define_mask('container')
        self.resource.mask |should| equal_to('container')

