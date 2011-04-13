import unittest
from should_dsl import should
from configurator.rule_checker import RuleChecker
from domain.node.person import Person
import bank_system.decorators
import configurator.rule_checker_imports


class RuleCheckerSpec(unittest.TestCase):

    def setUp(self):
        self.a_person = Person()
        self.rule_checker = RuleChecker()

    def it_finds_decorators(self):
        #it works with ordinary modules
        self.rule_checker.find_decorators(bank_system.decorators.bank_account_decorator)
        self.rule_checker |should| have(1).decorators
        self.rule_checker.decorators = []
        self.rule_checker.find_decorators(bank_system.decorators.credit_analyst_decorator)
         #credit_analyst_decorator imports bank_account_decorator => two decorators in the namespace
        self.rule_checker |should| have(2).decorators
        self.rule_checker.decorators = []
        #it works with configurator.rule_checker_imports, a pure import module
        self.rule_checker.find_decorators(configurator.rule_checker_imports)
        self.rule_checker |should| have(2).decorators

    def it_checks_rules(self):
        self.rule_checker.find_decorators(configurator.rule_checker_imports)
        self.rule_checker.check_rules(self.a_person)
        self.rule_checker |should| have(1).allowable_decorators
        self.rule_checker |should| have(1).broken_rules

