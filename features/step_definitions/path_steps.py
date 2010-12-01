# -*- coding: utf-8 -*-
from lettuce import step, world
from domain.path import Path
from domain.movement import Movement

@step(u'Given that I need to configure a path to reflect a given business process')
def given_that_I_need_to_configure_a_path_to_reflect_a_given_business_process(self):
    pass

@step(u'When I map path mask to (.+)')
def when_i_map_path_mask_to_business_process(step, business_process):
    world.path = Path()

@step(u'Then the path mask should be (.+)')
def then_the_path_mask_should_be_business_process(step, business_process):
    world.path.mask = business_process

@step(u'Given that I want to include an already configured movement to a path')
def given_that_i_want_to_include_an_already_configured_movement_to_a_path(step):
    world.configured_movement = Movement()

@step(u'When when I select a given (.+)')
def when_when_i_select_a_given_movement(step, movement):
    #I need a configured movement here - right now only with a mask
    world.configured_movement.mask = movement

@step(u'Then this movement is included into the path')
def then_this_movement_is_included_into_the_path(step):
    #world.path.movements.append(world.configured_movement)
    pass

