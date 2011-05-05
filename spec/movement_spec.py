import unittest
from should_dsl import should, should_not
from domain.node.person import Person
from domain.movement.movement import Movement
from domain.supportive.association_error import AssociationError

class MovementSpec(unittest.TestCase):

    def it_checks_source_and_destination(self):
        a_node = Person()
        non_node = "I am not a Node"
        movement = Movement()
        (movement.set_source, a_node) |should_not| throw(AssociationError)
        (movement.set_destination, a_node) |should_not| throw(AssociationError)
        (movement.set_source, non_node) |should| throw(AssociationError)
        (movement.set_destination, non_node) |should| throw(AssociationError)

