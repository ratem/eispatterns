class Resource(object):
    def __init__(self):
        self.mask = None
        self.unit = None

    def define_mask(self, concrete_concept):
        self.mask = concrete_concept

