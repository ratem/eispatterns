from domain.resource.resource import Resource


class WorkItem(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.unit = 'unit'

