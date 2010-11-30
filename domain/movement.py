#A Movement has the attributes:
# - Source (Node)
# - Destination (Node)
# - Resource (Resource)
# - Quantity (float)
#

class Movement(object):
    #default constructor - I cannot live with it
    def __init__(self):
        self.mask        = None
        self.source      = None
        self.destination = None
        self.resource    = None
        self.quantity    = 0.0

    def defineMask(self, concrete_concept):
        self.mask = concrete_concept

    def defineSource(self, source):
        self.source = source

    def defineDestination(self, destination):
        self.destination = destination

    def defineResource(self, resource):
        self.resource = resource

    def defineQuantity(self, quantity):
        self.quantity = quantity

