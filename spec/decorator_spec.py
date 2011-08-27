import unittest
from should_dsl import should
from domain.supportive.rule_manager import RuleManager
from domain.supportive.contract_error import ContractError
from domain.base.decorator import Decorator
from domain.node.person import Person


class FakeDecorator(Decorator):
    '''Fake Decorator for testing purposes'''
    decoration_rules = ['should_be_instance_of_person']
    def __init__(self):
        Decorator.__init__(self)

class DecoratorSpec(unittest.TestCase):
    def it_decorates(self):
        a_decorator = FakeDecorator()
        a_person = Person()
        a_decorator.decorate(a_person)
        a_person.decorators |should| contain("Fake Decorator for testing purposes")
        FakeDecorator.decoration_rules = ['xxxxx']
        (RuleManager.get_instance().check_decoration_rules, a_decorator, a_person) |should| throw(AttributeError)

