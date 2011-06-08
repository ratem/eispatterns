from datetime import datetime
from should_dsl import should
from domain.movement.movement import Movement
from domain.node.node import Node
from domain.supportive.association_error import AssociationError


class Process(Movement):
    def __init__(self, name=None):
        self.name = name
        #composition
        self.movements = {}
        #aggregation
        self.nodes = {}

    def insert_movement(self, key, movement):
        try:#a process should be passed as a movement too, check what could happen
            movement |should| be_instance_of(Movement)
        except:
            raise AssociationError('Movement instance expected, instead %s passed' % type(movement))
        self.movements[key] = movement

    def insert_node(self, key, node):
        try:#an organization should be passed as a node too, check what could happen
            node |should| be_instance_of(Node)
        except:
            raise AssociationError('Node instance expected, instead %s passed' % type(node))
        self.nodes[key] = node

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
        logger.store_execution_arguments(*arguments)
        activity_start = datetime.now()
        try:
          activity_result = logger.activity_associated_method(actor,*arguments)
          #workaround: Fluidity's transitions need be explicitly called to change state -> need refactoring
          logger.activity()
        except:
          raise
        else:
          activity_end = datetime.now()
        return {'actor':actor, 'result':activity_result, 'start': activity_start, 'end':activity_end}

