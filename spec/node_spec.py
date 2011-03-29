import unittest
from should_dsl import should
#from ludibrio import Stub
from domain.node.node import Node
from domain.resource.resource import Resource
from domain.supportive.contract_error import ContractError


class NodeSpec(unittest.TestCase):

    def setUp(self):
        self.a_node = Node()
        self.a_resource = Resource()

    def it_receives_a_resource(self):
        #should not work
        non_resource = "I am not a Resource"
        (self.a_node.receive_resource, non_resource,'anything') |should| throw(ContractError)
        #test doubles won't work given type checking rules, using classic
        self.a_node.receive_resource('resource key', self.a_resource)
        self.a_node.input_area |should| contain('resource key')

    def it_transfers_a_resource(self):
        self.a_node.receive_resource('resource key', self.a_resource)
        self.a_node.transfer('resource key', 'input', 'processing')
        #self.a_node.processing_area |should| contain('resource key')

