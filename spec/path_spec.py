import unittest
from should_dsl import should
from ludibrio import Dummy
from domain.movement import Movement
from domain.path import Path

class PathSpec(unittest.TestCase):

    def setUp(self):
        self.path = Path()

    def it_maps_a_given_business_process_to_its_mask(self):
        self.path.define_mask('sale')
        self.path.mask |should| equal_to('sale')

    def it_includes_a_configured_movement_to_its_list_of_movements(self):
        #At this point only a dummy movement is needed
        self.movement = Dummy()
        self.path.include_movement(self.movement)
        self.path.movements |should| include(self.movement)

    def it_includes_a_predecessor_to_a_movement(self):
        self.path.movements = []
        self.movement = Movement()
        self.path.include_movement(self.movement)
        self.predecessor = Movement()
        self.path.include_movement(self.predecessor)
        self.path.define_predecessor(self.movement, self.predecessor)
        self.path.movements[0].predecessors[0] |should| equal_to(self.predecessor)

