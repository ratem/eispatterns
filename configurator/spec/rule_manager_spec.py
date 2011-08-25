import unittest
from should_dsl import should
from configurator.rule_manager import RuleManager
from domain.base.decorator import Decorator
from domain.node.person import Person


class SomeDecorator(Decorator):
    '''Some Decorator'''
    rule_manager = RuleManager()
    decoration_rules = ['should_be_instance_of_person']

    def __init__(self):
        Decorator.__init__(self)

    #Will go to Decorator superclass
    def decorate(self, decorated):
        passed, approved_rules, refused_rules = self.__class__.rule_manager.check_decoration_rules(self.__class__, decorated)
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

    def it_is_a_singleton(self):
        a_rule_manager = RuleManager()
        another_rule_manager = RuleManager()
        another_rule_manager |should| be(a_rule_manager)

    def it_check_decoration_rules(self):
        a_person = Person()
        passed, approved_rules, refused_rules = SomeDecorator.rule_manager.check_decoration_rules(SomeDecorator, a_person)
        passed |should| equal_to(True)
        approved_rules |should| contain('''Associated object should be instance of Person''')
        refused_rules |should| equal_to(None)
        SomeDecorator.decoration_rules = ['an inexistent rule']
        (SomeDecorator.rule_manager.check_decoration_rules, SomeDecorator, a_person) |should| throw(AttributeError)
        #tear down
        SomeDecorator.decoration_rules = ['should_be_instance_of_person']

    def it_checks_a_rule(self):
        a_person = Person()
        SomeDecorator.rule_manager.check_rule('should_be_instance_of_person', a_person) |should| equal_to(True)
        SomeDecorator.rule_manager.check_rule('should_be_instance_of_machine', a_person) |should| equal_to(False)
        (SomeDecorator.rule_manager.check_rule, 'wrong rule...', a_person) |should| throw(AttributeError)

