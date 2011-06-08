from datetime import datetime
from should_dsl import should
from domain.movement.movement import Movement
from domain.node.node import Node
from domain.supportive.association_error import AssociationError


class Process(Movement):
    def __init__(self, name=None):
        self.name = name
        self.movements = {}

    def insert_movement(self, key, movement):
        try:#a process should be passed as a movement too, check what could happen
            movement |should| be_instance_of(Movement)
        except:
            raise AssociationError('Movement instance expected, instead %s passed' % type(movement))
        self.movements[key] = movement

    def configure_activity(self, source, destination, activity, method):
        '''Configures an activity (activity, transition, state's action...)'''
        logger = Movement()
        logger.set_source(source)
        logger.set_destination(destination)
        logger.activity = activity
        logger.activity_associated_method = method
        self.insert_movement(activity.__name__,logger)
        return logger

    #Transformations & Transportations must be rethinked
    def run_activity(self, logger, actor, *arguments):
        ''' Runs an activity using given arguments and logging context data'''
        execution_arguments = []
        for argument in arguments:
            execution_arguments.append(argument)
        activity_start = datetime.now()
        try:
          activity_result = logger.activity_associated_method(actor,*arguments)
          #ugly workaround: Fluidity's transitions need be explicitly called to change state
          logger.activity()
        except:
          activity_end = None
          activity_result = None
          raise
        else:
          activity_end = datetime.now()
        return {'actor':actor, 'arguments': execution_arguments, 'result':activity_result, 'start': activity_start, 'end':activity_end}

