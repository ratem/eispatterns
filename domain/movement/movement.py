from inspect import ismethod
from should_dsl import should
from domain.base.decorable import Decorable
from domain.node.node import Node
from domain.supportive.contract_error import ContractError


class Movement(Decorable):
    def __init__(self):
        Decorable.__init__(self)
        self.source = None
        self.destination = None
        self.operation = None
        self.parameters = {}

    def set_source(self, source):
        try:
            source |should| be_instance_of(Node)
        except:
            raise ContractError('Node instance expected, instead %s passed' % type(movement))
        self.source = source

    def set_destination(self, destination):
        try:
            destination |should| be_instance_of(Node)
        except:
            raise ContractError('Node instance expected, instead %s passed' % type(movement))
        self.destination = destination

    #conditions for a operation: be a @operation, be a Decorator or Node method
    def set_operation(self, operation):
        if hasattr(operation,'category'):
            self.operation = operation
            return True
        else:
            return False

