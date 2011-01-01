import unittest
from should_dsl import should
from ludibrio import Stub
from domain.movement import Movement

class MovementSpec(unittest.TestCase):

    def setUp(self):
        self.movement = Movement()
        #will need to set a configuration object many times
        with Stub() as self.configuration:
            self.configuration.mask >> 'payment'
            self.configuration.version >> 'monthly'
            self.configuration.type >> 'financial'
            self.configuration.description >> 'a payment from the company to an employee'
            self.configuration.source_node_mask >> 'company'
            self.configuration.source_node_mask_version >> 'a1'
            self.configuration.destination_node_mask >> 'developer'
            self.configuration.destination_node_mask_version >> 'junior 1.0'
            self.configuration.resource_mask >> 'money'
            self.configuration.resource_mask_version >> 'american dollars'

    def simulates_some_movement_performing(self):
        return 'I can perform'

    def it_defines_how_a_movement_performs(self):
        #since nothing was done, process_resources must be an alias for todo()
        self.movement.perform |should| equal_to(self.movement.todo)
        #now it will learn how to perform
        self.movement.define_how_to_perform(self.simulates_some_movement_performing)
        self.movement.perform |should| equal_to(self.simulates_some_movement_performing)

    def it_configures_a_movement(self):
        self.movement.configure(self.configuration)
        #We need a way of doing self.movement.configuration |should| equal_to(self.configuration)
        #more productively...
        self.movement.configuration.mask |should| equal_to('payment')
        self.movement.configuration.version |should| equal_to('monthly')
        self.movement.configuration.type |should| equal_to('financial')
        self.movement.configuration.description |should| equal_to('a payment from the company to an employee')
        self.movement.configuration.source_node_mask |should| equal_to('company')
        self.movement.configuration.source_node_mask_version |should| equal_to('a1')
        self.movement.configuration.destination_node_mask |should| equal_to('developer')
        self.movement.configuration.destination_node_mask_version |should| equal_to('junior 1.0')
        self.movement.configuration.resource_mask |should| equal_to('money')
        self.movement.configuration.resource_mask_version |should| equal_to('american dollars')

    def it_sets_a_source_node(self):
        self.movement.configure(self.configuration)
        with Stub() as source:
            source.mask    >> 'company'
            source.version >> 'a1'
            source.title   >> 'My Company'
        self.movement.set_source_node(source)
        #self.movement.source_node |should| equal_to(source)
        self.movement.source_node.title |should| equal_to('My Company')

