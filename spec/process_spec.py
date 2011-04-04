import unittest
from should_dsl import should
#from ludibrio import Stub
from domain.node.node import Node
from domain.movement.movement import Movement
from domain.movement.process import Process
from domain.resource.operation import operation
from domain.supportive.contract_error import ContractError

class ProcessSpec(unittest.TestCase):

    def setUp(self):
        self.a_client = Node()
        self.the_company = Node()
        self.a_process = Process(self.the_company, self.a_client)
        self.a_processing_unit = Node()
        self.a_movement = Movement(self.a_processing_unit, self.a_processing_unit)

    def it_inserts_a_movement(self):
        #should not work
        non_movement = "I am not a Movement"
        (self.a_process.insert_movement, 'Ops!',non_movement) |should| throw(ContractError)
        #test doubles won't work given type checking rules, using classic
        self.a_process.insert_movement('A movement', self.a_movement)
        self.a_process.movements |should| contain('A movement')

    def it_inserts_a_node(self):
        #should not work
        non_node = "I am not a Node"
        (self.a_process.insert_node, 'Ops!', non_node) |should| throw(ContractError)
        #test doubles won't work given type checking rules, using classic
        self.a_process.insert_node('A company processing unit', self.a_processing_unit)
        self.a_process.nodes |should| contain('A company processing unit')

