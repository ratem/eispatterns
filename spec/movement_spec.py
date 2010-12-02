import unittest
from should_dsl import should
from domain.movement import Movement
from domain.node import Node
from domain.resource import Resource

class MovementSpec(unittest.TestCase):

    def setUp(self):
        self.movement = Movement()

    #how can I parametrize these tests?
    def it_maps_a_given_concrete_movement_to_its_mask(self):
        self.movement.define_mask('shipment')
        self.movement.mask |should| equal_to('shipment')

    def it_maps_a_given_source_type_to_source(self):
        source_node = Node()
        source_node.define_mask('inventory')
        self.movement.source = source_node
        self.movement.source.mask |should| equal_to('inventory')

    def it_maps_a_given_destination_type_to_movement_to_destination(self):
        destination_node = Node()
        destination_node.define_mask('shipment bay')
        self.movement.destination = destination_node
        self.movement.destination.mask |should| equal_to('shipment bay')

    def it_maps_a_given_resource_type_to_resource(self):
        resource = Resource()
        resource.define_mask('container')
        self.movement.resource = resource
        self.movement.resource.mask |should| equal_to('container')

    def it_sets_the_quantity(self):
        self.movement.define_quantity(10)
        self.movement.quantity |should| equal_to(10)

