# -*- coding: utf-8 -*-
from lettuce import step, world
from should_dsl import should
from domain.path import Path
from domain.movement import Movement

@step(u'Given I need to configure a path to reflect a given business process')
def given_i_need_to_configure_a_path_to_reflect_a_given_business_process(step):
    world.path = Path()

@step(u'When I map path mask to (.+)')
def when_i_map_path_mask_to_business_process(step, business_process):
    world.path.define_mask(business_process)

@step(u'Then the path mask should be (.+)')
def then_the_path_mask_should_be_business_process(step, business_process):
    world.path.mask |should| equal_to(business_process)

@step(u'Given I have a configured (.+)')
def given_i_have_a_configured_path(step, path):
    #new scenario, new objects
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

#@step(u'Given I have a configured path')
# a function with the same name already exists in another scenario, thus an
# error will pop if I include this call, so I am forced to use the already
# created path object

@step(u'And I have at least two configured movements in this path')
def and_i_have_at_least_two_configured_movements_in_this_path(self):
    #I already have a movement in this path, I need to include only one
    another_movement = Movement()
    another_movement.define_mask('order payment')
    world.path.include_movement(another_movement)
    len(world.path.movements) |should| equal_to(2)

@step(u'When I select (.+) as predecessor of (.+)')
def when_i_select_predecessor_as_predecessor_of_movement(step, predecessor, movement):
    #GUI operation goes here
    pass

@step(u'And I include (.+) as predecessor of (.+)')
def and_i_include_predecessor_as_predecessor_of_movement(step, predecessor, movement):
    world.path.movements[0].predecessors.append(predecessor)

@step(u'Then (.+) should be a predecessor of (.+)')
def then_predecessor_should_be_a_predecessor_of_movement(step, predecessor, movement):
    world.path.movements[0].predecessors[0] |should| equal_to(predecessor)

