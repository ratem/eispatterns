from domain.base.decorable import Decorable


class Node(Decorable):
    def __init__(self):
        Decorable.__init__(self)
        self.resources_in_input_area = []
        self.resources_in_processing_area = []
        self.resources_in_output_area = []
        self.tag = None
        self.location = None

