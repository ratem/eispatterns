class Movement(object):

    @classmethod
    def create_as(cls, concept):
        movement = cls()
        movement.mask = concept
        return movement

