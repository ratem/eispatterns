from domain.resource import Resource


class Material(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.quantity = 0.0

