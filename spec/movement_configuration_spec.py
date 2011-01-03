import unittest
from should_dsl import should
from domain.movement_configuration import MovementConfiguration

class MovementConfigurationSpec(unittest.TestCase):

    def setUp(self):
        self.movement_configuration = MovementConfiguration()

    def it_parses_a_movement_configuration(self):
        '''I am not parsing a movement configuration in fact'''

    def it_persists_a_movement_configuration(self):
        '''I am not persisting a movement configuration in fact'''

    def it_retrieves_a_movement_configuration_from_some_storage(self):
        '''I am not retrieving a resource configuration in fact'''

    def it_lists_the_available_configurations_for_a_given_movement(self):
        '''I am not listing the available configurations in fact'''

