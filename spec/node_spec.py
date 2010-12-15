import unittest
from should_dsl import should
from ludibrio import Stub
from domain.node import Node

class NodeSpec(unittest.TestCase):

    def it_defines_how_a_node_processes_resources(self):
        #defines a callable for implementing 'process', even in runtime
        pass

    def it_defines_a_location_of_a_node(self):
        #to be defined at instantiation time
        pass

