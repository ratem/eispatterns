#A Movement has the attributes:
# - Source (Node)
# - Destination (Node)
# - Resource (Resource)
# - Quantity (float)
#

class Movement(object):
    #default constructor
    def __init__(self):
        self.mask        = None
        self.source      = None
        self.destination = None
        self.resource    = None
        self.quantity    = 0.0

    def define_mask(self, concrete_concept):
        self.mask = concrete_concept

    def define_source(self, source):
        self.source = source

    def define_destination(self, destination):
        self.destination = destination

    def define_resource(self, resource):
        self.resource = resource

    def define_quantity(self, quantity):
        self.quantity = quantity

