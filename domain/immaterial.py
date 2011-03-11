from domain.resource import Resource


class Immaterial(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.duration = 0.0

