import unittest
from should_dsl import should
from domain.movement import Movement
from domain.path import Path

class PathSpec(unittest.TestCase):

    def setUp(self):
        self.path = Path()
        self.movement = Movement()
        self.movement.defineMask('shipment')

    #how can I parametrize these tests?
    def it_maps_a_given_business_process_to_its_mask(self):
        self.path.defineMask('sale')
        self.path.mask |should| equal_to('sale')

    def it_includes_a_configured_movement_to_its_list_of_movements(self):
        self.path.includeMovement(self.movement)

