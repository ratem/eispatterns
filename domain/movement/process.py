from should_dsl import should
from domain.movement.movement import Movement
from domain.supportive.contract_error import ContractError


class Process(Movement):
    def __init__(self):
        Movement.__init__(self)
        self.movements = []

    def insert_movement(self, movement):
        try:#process should be passed as a movement too, check what could happen
            movement |should| be_instance_of(Movement)
        except:
            raise ContractError('Movement instance expected, instead %s passed' % type(movement))
        self.movements.append(movement)

