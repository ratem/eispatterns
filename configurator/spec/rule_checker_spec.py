import unittest
from should_dsl import should
from configurator.rule_checker import RuleChecker
from domain.node.person import Person
import configurator.rule_checker_imports
import eispatterns_examples.bank_system.decorators


class RuleCheckerSpec(unittest.TestCase):
    '''Currently you need to have eispatterns_example.bank_system installed to run these tests'''
    def setUp(self):
        self.a_person = Person()
        self.rule_checker = RuleChecker()

    def tearDown(self):
        self.rule_checker.decorators = []

    def it_finds_decorators(self):
        #it works with ordinary modules
        self.rule_checker.find_decorators(eispatterns_examples.bank_system.decorators.bank_account_decorator)
        self.rule_checker |should| have(1).decorators
        self.rule_checker.decorators = []
        self.rule_checker.find_decorators(eispatterns_examples.bank_system.decorators.credit_analyst_decorator)
        #credit_analyst_decorator imports bank_account_decorator and
        #employee_decorator => two decorators in the namespace
        self.rule_checker |should| have(3).decorators
        self.rule_checker.decorators = []
        #it works with configurator.rule_checker_imports, a pure import module
        self.rule_checker.find_decorators(configurator.rule_checker_imports)
        self.rule_checker |should| have(3).decorators

    def it_checks_rules(self):
        #configuration for getting the specific rules
        from domain.supportive.rule_manager import RuleManager
        from bank_system.rules.bank_system_rule_base import BankSystemRuleBase
        self.rule_checker.find_decorators(configurator.rule_checker_imports)
        RuleManager.rule_base = BankSystemRuleBase()
        #check it!
        self.rule_checker.check_rules(self.a_person)
        self.rule_checker.allowable_decorators |should| contain(eispatterns_examples.bank_system.decorators.employee_decorator.EmployeeDecorator)
        self.rule_checker.non_allowable_decorators |should| include_in_any_order([eispatterns_examples.bank_system.decorators.bank_account_decorator.BankAccountDecorator, eispatterns_examples.bank_system.decorators.credit_analyst_decorator.CreditAnalystDecorator])
        self.rule_checker.broken_rules |should| include_in_any_order([['Associated object should be instance of Machine'],['Associated object should be previously decorated by Employee']])

