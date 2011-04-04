from datetime import datetime
from should_dsl import should
from domain.base.decorable import Decorable
from domain.node.node import Node
from domain.supportive.contract_error import ContractError


class Movement(Decorable):
    def __init__(self, source, destination):
        Decorable.__init__(self)
        try:
            source |should| be_instance_of(Node)
        except:
            raise ContractError('Source: Node instance expected, instead %s passed' % type(source))
        self.source = source
        try:
            destination |should| be_instance_of(Node)
        except:
            raise ContractError('Destination: Node instance expected, instead %s passed' % type(destination))
        self.destination = destination

