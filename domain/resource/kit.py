from domain.resource.resource import Resource


class Kit(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.resources = []

