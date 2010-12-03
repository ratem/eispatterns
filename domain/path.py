#A Path must keep a list of previously configured movements. Every movement in a
#path must know about its predecessors and how many times it was executed
#in the path

class Path(object):
    def __init__(self):
        self.mask         = None
        self.movements    = []

    def define_mask(self, concrete_concept):
        self.mask = concrete_concept

    def include_movement(self, movement):
#       '''Only when enters a path, a movement needs to know about how many
#        times it was executed and its list of predecessors '''
#        movement.times_executed = 0
#        movement.predecessors = []
        self.movements.append(movement)

