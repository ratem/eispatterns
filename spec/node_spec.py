import unittest
from should_dsl import should
from ludibrio import Stub
from domain.node import Node

class NodeSpec(unittest.TestCase):

    def setUp(self):
        self.node = Node()

    def simulates_some_resource_processing(self):
        return 'I am able to process resources'

    def it_defines_how_a_node_processes_resources(self):
        #since nothing was done, process_resources must be an alias for todo()
        self.node.process_resources |should| equal_to(self.node.todo)
        #now it will learn how to process resources
        self.node.define_how_to_process_resources(self.simulates_some_resource_processing)
        self.node.process_resources |should| equal_to(self.simulates_some_resource_processing)

    def it_defines_the_location_of_a_node(self):
        '''I am not really testing the definition of a location for a resource yet'''
        pass

