# -*- coding: utf-8 -*-
from lettuce import step

@step(u'Given that I need to configure a movement as a (.+)')
def given_that_i_need_to_configure_a_movement_as_a(step, new_concept):
    assert False, 'This step must be implemented'

@step(u'When I map movement source to (.+)')
def when_i_map_movement_source_to(step, source_type):
    assert False, 'This step must be implemented'

@step(u'And I map movement destination to (.+)')
def and_i_map_movement_destination_to(step, destination_type):
    assert False, 'This step must be implemented'

@step(u'And I map movement resource to (.+)')
def and_i_map_movement_resource_to(step, resource_type):
    assert False, 'This step must be implemented'

@step(u'And I map movement quantity to (.+)')
def and_i_map_movement_quantity_to(step, quantity_type):
    assert False, 'This step must be implemented'

@step(u'Then I create a new Movement mask with (.+)')
def then_i_create_a_new_movement_mask_with(step, source_type):
    assert False, 'This step must be implemented'

@step(u"And new concept's destination type is of (.+)")
def and_new_concept_destination_type_is_of(step, destination_type):
    assert False, 'This step must be implemented'

@step(u"And new concept's resource type is of (.+)")
def and_new_concept_resource_type_is_of(step, resource_type):
    assert False, 'This step must be implemented'

@step(u"And new concept's quantity type is (.+)")
def and_new_concept_quantity_type_is(step, quantity_type):
    assert False, 'This step must be implemented'

