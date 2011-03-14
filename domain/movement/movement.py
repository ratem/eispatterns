from domain.base.decorable import Decorable


class Movement(Decorable):
    def __init__(self):
        Decorable.__init__(self)
        self.source = None
        self.destination = None
        self.quantity = 0.0

