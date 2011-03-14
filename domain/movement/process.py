from domain.movement.movement import Movement


class Process(Movement):
    def __init__(self):
        Movement.__init__(self)
        self.movements = []

