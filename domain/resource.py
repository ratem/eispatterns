from domain.decorable import Decorable

class Resource(Decorable):

    def __init__(self):
        Decorable.__init__(self)
        self.unit = None

