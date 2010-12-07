# -*- coding: utf-8 -*-
from lettuce import step, world
from should_dsl import should
from domain.movement import Movement
from domain.connection import Connection

@step(u'Given I need to configure a connection as a (.+)')
def given_i_need_to_configure_a_connection_as_a_new_type_of_connection(step, new_type_of_connection):
    world.connection = Connection()
    world.connection.define_mask('Payment is condition for Shipment')

@step(u'When I map left hand to (.+)')
def when_i_map_left_hand_to_left_hand_movement(step, left_hand_movement):
    world.left_hand_movement = Movement()
    world.left_hand_movement.define_mask(left_hand_movement)
    world.connection.define_left_hand(left_hand_movement)

@step(u'And I map right hand to (.+)')
def and_i_map_right_hand_to_right_hand_movement(step, right_hand_movement):
    world.right_hand_movement = Movement()
    world.right_hand_movement.define_mask(right_hand_movement)
    world.connection.define_right_hand(right_hand_movement)

@step(u'And I map binding type to (.+)')
def and_i_map_binding_type_to_binding_type(step, binding_type):
    world.connection.define_binding_type(binding_type)

@step(u'And I map binding time to (.+)')
def and_i_map_binding_time_to_binding_time(step, binding_time):
    world.connection.define_binding_time(binding_time)

@step(u'Then the connection mask should be (.+)')
def then_the_connection_mask_should_be_new_type_of_connection(step, new_type_of_connection):
    world.connection.mask |should| equal_to(new_type_of_connection)

@step(u"And new connection's left hand should be of (.+)")
def and_new_connection_left_hand_should_be_of_left_hand_movement(step, left_hand_movement):
    world.connection.left_hand |should| equal_to(left_hand_movement)

@step(u"And new connection's right hand type should be of (.+)")
def and_new_connection_right_hand_type_should_be_of_right_hand_movement(step, right_hand_movement):
    world.connection.right_hand |should| equal_to(right_hand_movement)

@step(u"And new connection's binding type should be of (.+)")
def and_new_connection_binding_type_should_be_of_binding_type(step, binding_type):
    world.connection.binding_type |should| equal_to(binding_type)

@step(u"And new connection's binding time should be (.+)")
def and_new_connection_binding_time_should_be_binding_time(step, binding_time):
    world.connection.binding_time |should| equal_to(binding_time)

