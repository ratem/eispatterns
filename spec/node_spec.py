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

    def it_transfers_a_resource(self):
        self.a_node.input_area['resource key'] = self.a_resource
        #from input to processing
        self.a_node.transfer('resource key', 'input', 'processing')
         #one way of testing
        self.a_node.processing_area |should| contain('resource key')
         #another way of testing
        self.a_node.processing_area['resource key'] |should| be(self.a_resource)
        #from processing to output
        self.a_node.transfer('resource key', 'processing', 'output')
        self.a_node.output_area |should| contain('resource key')
        #from output to log
        self.a_node.transfer('resource key', 'output', 'log')
        self.a_node.log_area |should| contain('resource key')

    def it_moves_a_resource_between_two_nodes(self):
        another_node = Node()
        self.a_node.output_area['resource'] = self.a_resource
        self.a_node.output_area['non_resource'] = "I am not a Resource"
        #should not work
        (Node.move_resource, 'wrong key', self.a_node, another_node) |should| throw(KeyError)
        (Node.move_resource, 'non_resource', self.a_node, another_node) |should| throw(ContractError)
        #should work
        Node.move_resource('resource', self.a_node, another_node)
        another_node.input_area |should| include('resource')

