import unittest
from should_dsl import should
#from ludibrio import Stub
from configurator.rule_checker import RuleChecker
from domain.node.person import Person
import bank_system.decorators
import configurator.import_decorators


class RuleCheckerSpec(unittest.TestCase):

    def setUp(self):
        self.a_person = Person()
        self.rule_checker = RuleChecker()

    def test_it_finds_decorators(self):
        #it works with ordinary modules
        self.rule_checker.find_decorators(bank_system.decorators.bank_account_decorator)
        self.rule_checker.decorators |should| have(1).item
        self.rule_checker.decorators = []
        self.rule_checker.find_decorators(bank_system.decorators.credit_analyst_decorator)
         #credit_analyst_decorator imports bank_account_decorator => two decorators in the namespace
        self.rule_checker.decorators |should| have(2).items
        self.rule_checker.decorators = []
        #it works with configurator.import_decorators, a import module
        self.rule_checker.find_decorators(configurator.import_decorators)
        self.rule_checker.decorators |should| have(2).items

    def test_it_finds_decorators_rules(self):
        self.rule_checker.find_decorators(bank_system.decorators.bank_account_decorator)
        for decorator in self.rule_checker.decorators:
            self.rule_checker.find_rules(decorator)
        self.rule_checker.rules |should| have(1).rules

    def test_it_checks_which_decorators_can_decorate_a_node(self):
        self.rule_checker.can_decorate(self.a_person)
        self.rule_checker.allowable_decorators |should| contain('Credit Analyst')

