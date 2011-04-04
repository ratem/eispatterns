from datetime import datetime
from domain.movement.movement import Movement


class Transformation(Movement):
    def __init__(self, source, destination):
        Movement.__init__(self, source, destination)

    #conditions for a transformation: be an @operation, ??be a Decorator or Node method??
    def set_action(self, operation):
        if hasattr(operation,'category'):
            self.action = operation
            return True
        else:
            return False

    def perform(self, *arguments):
        self.datetime = datetime.now()
        self.action(*arguments)

