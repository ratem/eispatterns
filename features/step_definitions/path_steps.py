# -*- coding: utf-8 -*-
from lettuce import step, world
from should_dsl import should
from domain.path import Path
from domain.movement import Movement
from domain.connection import Connection

@step(u'Given I need to configure a path to reflect a given business process')
def given_i_need_to_configure_a_path_to_reflect_a_given_business_process(step):
    world.path = Path()

@step(u'When I map path mask to (.+)')
def when_i_map_path_mask_to_business_process(step, business_process):
    world.path.define_mask(business_process)

@step(u'Then the path mask should be (.+)')
def then_the_path_mask_should_be_business_process(step, business_process):
    world.path.mask |should| equal_to(business_process)

@step(u'Given there is a configured (.+) available')
def given_there_is_a_configured_path_available(step, path):
    #new scenario, new objects ? but this doesn't work below...
    step.given('I need to configure a path to reflect a given business process')
    step.when('I map path mask to %s' % path)

@step(u'[Given|And] I want to include a configured movement to this path')
def and_i_want_to_include_a_configured_movement_to_this_path(step):
    world.configured_movement = Movement()

@step(u'When I select a given (.+)')
def when_i_select_a_given_movement(step, movement):
    #I need a configured movement here - right now only with a mask
    world.configured_movement.define_mask(movement)

@step(u'And I include this movement into the path')
def and_i_include_this_movement_into_the_path(step):
    world.path.include_movement(world.configured_movement)

@step(u'Then this movement should be into the path')
def then_this_movement_should_be_into_the_path(step):
    world.path.movements |should| include(world.configured_movement)

@step(u'And this (.+) has at least two movements')
def and_this_path_has_at_least_two_movements(step, path):
    world.another_movement = Movement()
    world.path.include_movement(world.another_movement)
    len(world.path.movements) |should| equal_to(2)

@step(u'And there is at least a (.+) which integrates two of these movements')
def and_there_is_at_least_a_connection_which_integrates_two_of_these_movements(step, connection):
    world.connection = Connection()
    world.connection.define_mask(connection)
    world.connection.define_left_hand(world.movement)
    world.connection.left_hand |should| equal_to(world.movement)
    world.connection.define_right_hand(world.another_movement)
    world.connection.right_hand |should| equal_to(world.another_movement)

@step(u'When I select a given (.+) to be included')
def when_i_select_a_given(self, connection):
    #GUI code goes here
    pass

@step(u'Then this connection should be included into the path')
def then_this_connection_should_be_included_into_the_path(step):
    world.path.include_connection(world.connection)
    world.path.connections |should| include(world.connection)

