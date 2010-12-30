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

    def it_configures_a_node(self):
        #Stubs a configuration object according to 'Development Department''A developer version junior
        #1.0 is a person, with less than three years of experience, able of
        #developing computer programs'
        with Stub() as configuration:
            configuration.mask >> 'developer'
            configuration.version >> 'junior 1.0'
            configuration.type >> 'person'
            configuration.description >> 'with less than three years of experience'
            configuration.processing_capabilities >> 'able of developing computer programs'
        #expected_configuration_attributes is defined only in subclasses, forced below
        self.node.expected_configuration_attributes = ['mask','version','type','description','processing_capabilities']
        self.node.configure(configuration)
        self.node.configuration.mask |should| equal_to('developer')
        self.node.configuration.version |should| equal_to('junior 1.0')
        self.node.configuration.type |should| equal_to('person')
        self.node.configuration.description |should| equal_to('with less than three years of experience')
        self.node.configuration.processing_capabilities |should| equal_to('able of developing computer programs')

    def it_defines_the_location_of_a_node(self):
        with Stub() as metanode:
            metanode.tag >> 'Development Department'
        self.node.location = metanode
        self.node.location.tag |should| equal_to('Development Department')

