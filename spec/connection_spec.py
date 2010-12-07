import unittest
from should_dsl import should
from ludibrio import Dummy
from domain.movement import Movement
from domain.connection import Connection

class ConnectionSpec(unittest.TestCase):

    def setUp(self):
        self.connection = Connection()

    def it_maps_a_given_concrete_connection_to_its_mask(self):
        self.connection.define_mask('Payment is condition for Shipment')
        self.connection.mask |should| equal_to('Payment is condition for Shipment')

    def it_includes_a_configured_movement_as_its_left_hand(self):
        self.left_hand_movement = Movement()
        self.left_hand_movement.define_mask('payment')
        self.connection.define_left_hand(self.left_hand_movement)
        self.connection.left_hand |should| equal_to(self.left_hand_movement)

    def it_includes_a_configured_movement_as_its_right_hand(self):
        self.right_hand_movement = Movement()
        self.right_hand_movement.define_mask('shipment')
        self.connection.define_right_hand(self.right_hand_movement)
        self.connection.right_hand |should| equal_to(self.right_hand_movement)

    def it_defines_its_binding_type(self):
        self.connection.define_binding_type('triggers before')
        self.connection.binding_type |should| equal_to('triggers before')

    def it_defines_its_binding_time(self):
        self.connection.define_binding_time('event dependent')
        self.connection.binding_time |should| equal_to('event dependent')

    def it_defines_things_todo(self):
        '''Defining what to do occurs during connection instantiation '''
        self.connection.todo = Dummy()

