#A Path must keep a list of previously configured movements. Every movement in a
#path must know about its predecessors and how many times it was executed
#in the path

class Path(object):
    def __init__(self):
        self.mask         = None
        self.movements    = []

    def defineMask(self, concrete_concept):
        self.mask = concrete_concept

    def includeMovement(self, movement):
#        movement.timesExecuted = 0
#        movement.predecessor = []
        self.movements.append(movement)

