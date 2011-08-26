import unittest
from should_dsl import should
from configurator.rule_manager import RuleManager
from domain.node.person import Person
from domain.base.decorator import Decorator


class SomeDecorator(Decorator):
    '''Some Decorator'''
    decoration_rules = ['should_be_instance_of_person']

    def __init__(self):
        Decorator.__init__(self)

    #Will go to Decorator superclass
    def decorate(self, decorated):
        passed, approved_rules, refused_rules = RuleManager.get_instance().check_decoration_rules(self,decorated)
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
        SomeDecorator.decoration_rules = ['xxxxx']
        (RuleManager.get_instance().check_decoration_rules, a_decorator, a_person) |should| throw(AttributeError)
        #tear down
        SomeDecorator.decoration_rules = ['should_be_instance_of_person']

    def it_is_a_singleton(self):
        a_rule_manager = RuleManager()
        another_rule_manager = RuleManager()
        another_rule_manager |should| be(a_rule_manager)
        RuleManager.get_instance() |should| be(a_rule_manager)

    def it_check_decoration_rules(self):
        a_person = Person()
        a_decorator = SomeDecorator()
        passed, approved_rules, refused_rules = RuleManager.get_instance().check_decoration_rules(SomeDecorator, a_person)
        passed |should| equal_to(True)
        approved_rules |should| contain('''Associated object should be instance of Person''')
        refused_rules |should| equal_to(None)
        SomeDecorator.decoration_rules = ['xxxxx']
        (RuleManager.get_instance().check_decoration_rules, SomeDecorator, a_person) |should| throw(AttributeError)
        #tear down
        SomeDecorator.decoration_rules = ['should_be_instance_of_person']

    def it_checks_a_rule(self):
        a_person = Person()
        RuleManager.get_instance().check_rule('should_be_instance_of_person', a_person) |should| equal_to(True)
        RuleManager.get_instance().check_rule('should_be_instance_of_machine', a_person) |should| equal_to(False)
        (RuleManager.get_instance().check_rule, 'wrong rule...', a_person) |should| throw(AttributeError)

