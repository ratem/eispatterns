from should_dsl import should
from datetime import datetime
from domain.movement.movement import Movement
from domain.supportive.association_error import AssociationError

class Transformation(Movement):

    def __init__(self, name=None, action=None):
        self.name = name
        self.action = action
#        self.from_state = from_state
#        self.to_state = to_state

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
        try:
            actor |should| be_instance_of(self.action.im_class)
        except:
            raise AssociationError("Actor should be %s, instead %s passed" % (self.action.im_class, type(actor)))
        self.actor = actor

