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

    def it_includes_a_configured_connection_to_its_list_of_connections(self):
        self.connection = Dummy()
        self.path.include_connection(self.connection)
        self.path.connections |should| include(self.connection)

    def it_defines_a_way_of_orchestrating_movements(self):
        '''Defining orchestration actions occurs during connection implementation '''
        self.path.orchestrate = Dummy()

