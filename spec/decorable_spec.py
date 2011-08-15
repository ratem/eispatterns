import unittest
from should_dsl import should
from domain.supportive.contract_error import ContractError
from domain.base.decorable import Decorable
from domain.base.decorator import Decorator

class FakeDecorator(Decorator):
    '''Fake Decorator for testing purposes'''
    def __init__(self):
        Decorator.__init__(self)

class DecorableSpec(unittest.TestCase):
    def setUp(self):
        self.a_node = Decorable()
        self.a_decorator = Decorator()

    def it_gets_decorated(self):
        self.a_node.decorate(self.a_decorator)
        self.a_node |should| have(1).decorators
        self.a_node.decoration_history |should| have(1).element

    def it_gest_undecorated(self):
        self.a_node.decorate(self.a_decorator)
        self.a_node.undecorate(self.a_decorator) |should| equal_to(True)
        self.a_node.undecorate('Something else') |should| equal_to(False)

