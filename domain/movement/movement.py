from datetime import datetime
from should_dsl import should
from domain.base.decorable import Decorable
from domain.node.node import Node
from domain.supportive.association_error import AssociationError


class Movement(Decorable):

    def set_source(self, source):
        try:
            source |should| be_instance_of(Node)
        except:
            raise AssociationError('Source: Node instance expected, instead %s passed' % type(source))
        self.source = source

    def set_destination(self, destination):
        try:
            destination |should| be_instance_of(Node)
        except:
            raise AssociationError('Destination: Node instance expected, instead %s passed' % type(destination))
        self.destination = destination

    def perform(self, *arguments):
        return 0

