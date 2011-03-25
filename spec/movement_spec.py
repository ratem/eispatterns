import unittest
from should_dsl import should
from ludibrio import Stub
from domain.node.person import Person
from domain.movement.movement import Movement
from domain.resource.operation import operation
from domain.supportive.contract_error import ContractError

class MovementSpec(unittest.TestCase):

    def setUp(self):
        self.a_movement = Movement()

    @operation(category='business')
    def an_operation(self, argument):
        return argument

    def non_operation(self):
        return 0

    def it_sets_a_source_node(self):
        #should not work
        a_source = "I am not a Node"
        (self.a_movement.set_source, a_source) |should| throw(ContractError)
        #test doubles won't work given type checking rules, using classic
        a_source = Person()
        self.a_movement.set_source(a_source)
        self.a_movement.source |should| equal_to(a_source)

    def it_sets_a_destination_node(self):
        #should not work
        a_destination = "I am not a Node"
        (self.a_movement.set_source, a_destination) |should| throw(ContractError)
        #test doubles won't work given type checking rules, using classic
        a_destination = Person()
        self.a_movement.set_destination(a_destination)
        self.a_movement.destination |should| equal_to(a_destination)

    def it_sets_an_operation(self):
        #should not work
        self.a_movement.set_operation(self.non_operation) |should| be(False)
        #should work
        self.a_movement.set_operation(self.an_operation)
        self.a_movement.operation |should| equal_to(self.an_operation)

    def it_runs_its_operation(self):
        #tests are not ran in order, thus setting operation "again"
        self.a_movement.set_operation(self.an_operation)
        #Movement.run() returns nothing...
        self.a_movement.run(10)

