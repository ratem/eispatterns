import unittest
from should_dsl import should
from ludibrio import Stub
from domain.node import Node
from domain.node_configuration import NodeConfiguration

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

    def it_configures_a_node(self):
        #a complete configuration
        configuration = NodeConfiguration()
        configuration.mask = 'developer'
        configuration.version = 'junior 1.0'
        configuration.category = 'person'
        configuration.description = 'with less than three years of experience'
        configuration.processing_capabilities = 'able of developing computer programs'
        self.node.configure(configuration)
        self.node.configuration |should| equal_to(configuration)

    def it_defines_the_location_of_a_node(self):
        with Stub() as metanode:
            metanode.tag >> 'Development Department'
        self.node.location = metanode
        self.node.location.tag |should| equal_to('Development Department')

