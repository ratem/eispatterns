class Node(object):
    def __init__(self):
        self.mask     = None
        self.location = None

    def define_mask(self,concrete_concept):
        self.mask = concrete_concept

