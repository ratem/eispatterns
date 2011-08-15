from datetime import datetime
from should_dsl import should
from domain.base.decorable import Decorable
from domain.node.node import Node
from domain.supportive.association_error import AssociationError


class Movement(Decorable):

    def __init__(self, name=None):
        self.name = name
        self.context = {}
        self.source = self.destination = None

    def set_source(self, source):
        try:
            source |should| be_instance_of(Node)
        except:
            raise AssociationError('Source: Node instance expected, instead %s passed' % type(source))
        self.source = source
        self._typify()

    def set_destination(self, destination):
        try:
            destination |should| be_instance_of(Node)
        except:
            raise AssociationError('Destination: Node instance expected, instead %s passed' % type(destination))
        self.destination = destination
        self._typify()

    def _typify(self):
        ''' Identifies if movement is a transformation or a transportation
            If one of source or destination is not defined yet, it will consider
            as a transportation from/to Null'''
        #In the future will use Category objects
        if self.source == self.destination:
            self.category = 'Transformation'
        else:
            self.category = 'Transportation'

    def is_transformation(self):
        return self.category == 'Transformation'

    def is_transportation(self):
        return self.category == 'Transportation'

