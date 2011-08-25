import unittest
from should_dsl import should
from configurator.rule_manager import RuleManager
from domain.base.decorator import Decorator
from domain.node.person import Person


class SomeDecorator(Decorator):
    '''Some Decorator'''
    rule_manager = RuleManager()

    def __init__(self):
        Decorator.__init__(self)

    #Will go to Decorator superclass
    def decorate(self, decorated):
        passed, approved_rules, refused_rules = self.__class__.rule_manager.check_rules_for_class(self.__class__, decorated)
        if passed:
           self.decorated = decorated
           self.decorated.decorate(self)
        return passed, approved_rules, refused_rules

class RuleManagerSpec(unittest.TestCase):
    #testing the generic decorate()
    def it_decorates(self):
        a_decorator = SomeDecorator()
        a_person = Person()
        a_decorator.decorate(a_person)
        a_person.decorators |should| contain("Some Decorator")

    def it_check_rules_for_class(self):
        a_person = Person()
        passed, approved_rules, refused_rules = SomeDecorator.rule_manager.check_rules_for_class(SomeDecorator, a_person)
        passed |should| equal_to(True)
        approved_rules |should| contain(RuleManager.should_be_instance_of_person)
        refused_rules |should| equal_to([])

