import unittest
from should_dsl import should
from domain.node import Node

class NodeSpec(unittest.TestCase):

    def setUp(self):
        self.node = Node()

    def it_maps_a_given_concrete_concept_to_its_mask(self):
        self.node.define_mask('inventory')
        self.node.mask |should| equal_to('inventory')

