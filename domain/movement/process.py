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

    def configure_activity(self, source, destination, method):
        '''Configures a process activity (activity, transition, state's action...)'''
        logger = Movement()
        logger.set_source(source)
        logger.set_destination(destination)
        #to perform: activity = method
        return method, logger

    def run_activity(self, actor, activity, *arguments):
        ''' Runs an activity using given arguments '''
        #Must check: transportations are different...
        activity_start = datetime.now()
        activity_result = activity(actor,*arguments)
        activity_end = datetime.now()
        return activity_result, activity_start, activity_end

