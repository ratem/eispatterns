from datetime import datetime
from domain.movement.movement import Movement


class Transportation(Movement):

    def __init__(self, name=None):
        self.name = name

    def perform(self, resource_key):
        self.datetime = datetime.now()
        try:
            resource = self.source.output_area.pop(resource_key)
        except KeyError:
            raise KeyError('Source Output Area has no %s' % resource_key)
        self.destination.input_area[resource_key] = resource

