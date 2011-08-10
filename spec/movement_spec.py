import unittest
from should_dsl import should, should_not
from domain.node.node import Node
from domain.movement.movement import Movement
from domain.supportive.association_error import AssociationError

class MovementSpec(unittest.TestCase):

    def setUp(self):
        self.a_node = Node()
        self.movement = Movement()

    def it_checks_source_and_destination(self):
        non_node = "I am not a Node"
        (self.movement.set_source, self.a_node) |should_not| throw(AssociationError)
        (self.movement.set_destination, self.a_node) |should_not| throw(AssociationError)
        (self.movement.set_source, non_node) |should| throw(AssociationError)
        (self.movement.set_destination, non_node) |should| throw(AssociationError)

    def it_typifies_itself(self):
        another_node = Node()
        self.movement.set_source(self.a_node)
        self.movement.set_destination(self.a_node)
        self.movement.typify()
        self.movement.category |should| equal_to('Transformation')
        self.movement.set_destination(another_node)
        self.movement.typify()
        self.movement.category |should| equal_to('Transportation')

