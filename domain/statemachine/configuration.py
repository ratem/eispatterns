from domain.movement.transformation import Transformation
from domain.movement.movement import Movement
from domain.movement.process import Process

class ProcessTemplate(object):

    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.states = [initial_state]
        self.transformations = []

    def transformation(self, name, action):
        self.transformations.append(Transformation(name, action))
        #self._add_states(from_state, to_state)

    def _add_states(self, *states):
        for state in states:
            if self.states.count(state) == 0:
                self.states.append(state)

