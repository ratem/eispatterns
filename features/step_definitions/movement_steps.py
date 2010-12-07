# -*- coding: utf-8 -*-
from lettuce import step, world
from should_dsl import should
from domain.movement import Movement

@step(u'Given I need to configure a movement as a (.+)')
def given_i_need_to_configure_a_movement_as_a(step, new_concept):
    world.movement = Movement()
    world.movement.mask = new_concept

@step(u'When I map movement source to (.+)')
def when_i_map_movement_source_to(step, source_type):
    world.movement.source_type = source_type

@step(u'And I map movement destination to (.+)')
def and_i_map_movement_destination_to(step, destination_type):
    world.movement.destination_type = destination_type

@step(u'And I map movement resource to (.+)')
def and_i_map_movement_resource_to(step, resource_type):
    world.movement.resource_type = resource_type

@step(u'And I map movement quantity to (.+)')
def and_i_map_movement_quantity_to(step, quantity_type):
    world.movement.quantity_type = quantity_type

@step(u'Then the movement mask should be (.+)')
def then_i_create_a_new_movement_mask_should_be(step, source_type):
    world.movement.mask |should| equal_to(source_type)

@step(u"And new concept's source type should be of (.+)")
def and_new_concept_source_type_is_of(step, source_type):
    world.movement.source_type |should| equal_to(source_type)

@step(u"And new concept's destination type should be of (.+)")
def and_new_concept_destination_type_is_of(step, destination_type):
    world.movement.destination_type |should| equal_to(destination_type)

@step(u"And new concept's resource type should be of (.+)")
def and_new_concept_resource_type_is_of(step, resource_type):
    world.movement.resource_type |should| equal_to(resource_type)

@step(u"And new concept's quantity type should be (.+)")
def and_new_concept_quantity_type_is_of(step, quantity_type):
    world.movement.quantity_type |should| equal_to(quantity_type)

