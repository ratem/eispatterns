import unittest
from should_dsl import should
#from ludibrio import Stub
from configurator.rule_checker import RuleChecker
from domain.node.person import Person
import bank_system.decorators

class RuleCheckerSpec(unittest.TestCase):

    def setUp(self):
        self.a_person = Person()
        self.rule_checker = RuleChecker()

    def it_checks_which_decorators_can_decorate_a_node(self):
        self.rule_checker.can_decorate(self.a_person)
        self.rule_checker.allowable_decorators |should| contain('Credit Analyst')

    def it_finds_decorators(self):
        self.rule_checker.find_decorators(bank_system.decorators.bank_account_decorator)
        self.rule_checker.decorators |should| have_at_least(1).items
        self.rule_checker.find_decorators(bank_system.decorators.credit_analyst_decorator)
        self.rule_checker.decorators |should| have_at_least(1).items
