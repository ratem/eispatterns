from domain.base.decorable import Decorable


class Node(Decorable):
    def __init__(self):
        Decorable.__init__(self)
        self.input_area = []
        self.processing_area = []
        self.output_area = []
        self.tag = None
        self.location = None

