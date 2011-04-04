import unittest
from should_dsl import should, should_not
from domain.node.person import Person
from domain.movement.movement import Movement
from domain.supportive.contract_error import ContractError

class MovementSpec(unittest.TestCase):

    def it_checks_source_and_destination(self):
        a_node = Person()
        non_node = "I am not a Node"
        #this also works...: Movement(source=a_node, destination=a_node) |should_not| throw(ContractError)
        (Movement, a_node, a_node) |should_not| throw(ContractError)
        (Movement,non_node, a_node) |should| throw(ContractError)
        (Movement,a_node, non_node) |should| throw(ContractError)

