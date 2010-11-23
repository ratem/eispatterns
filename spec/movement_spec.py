import unittest
from should_dsl import should
from domain.movement import Movement

class MovementSpec(unittest.TestCase):

    def it_maps_a_given_source_type_to_its_mask(self):
        movement = Movement.create_as('shipment')
        movement.mask |should| equal_to('shipment')

