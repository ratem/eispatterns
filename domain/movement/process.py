from should_dsl import should
from domain.movement.movement import Movement
from domain.node.node import Node
from domain.supportive.contract_error import ContractError


class Process(Movement):
    def __init__(self):
        #composition
        self.movements = {}
        #aggregation
        self.nodes = {}

    def insert_movement(self, key, movement):
        try:#a process should be passed as a movement too, check what could happen
            movement |should| be_instance_of(Movement)
        except:
            raise ContractError('Movement instance expected, instead %s passed' % type(movement))
        self.movements[key] = movement

    def insert_node(self, key, node):
        try:#an organization should be passed as a node too, check what could happen
            node |should| be_instance_of(Node)
        except:
            raise ContractError('Node instance expected, instead %s passed' % type(node))
        self.nodes[key] = node

    def configure(self, template):
        self.template = template
        self.states = template.states
        self.transformations = template.transformations
        for transformation in template.transformations:
            self.insert_movement(transformation.name, transformation)

