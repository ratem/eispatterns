from datetime import datetime
from domain.movement.movement import Movement
from domain.supportive.contract_error import ContractError


class Transformation(Movement):

    def __init__(self, name=None, from_state=None, to_state=None, action=None):
        self.name = name
        self.action = action
        self.from_state = from_state
        self.to_state = to_state

    #conditions for a transformation: be an @operation, ??be a Decorator or Node method??
    def set_action(self, operation):
        if hasattr(operation,'category'):
            self.action = operation
            return True
        else:
            return False

    def perform(self, *arguments):
        self.datetime = datetime.now()
        return self.action(self.actor, *arguments)


    def set_actor(self, actor):
        if not isinstance(actor, self.action.im_class):
            raise ContractError("Actor doesn't belong to expected type")
        self.actor = actor

