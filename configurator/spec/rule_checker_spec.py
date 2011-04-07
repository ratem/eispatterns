import unittest
from should_dsl import should
from ludibrio import Stub
from configurator.rule_checker import RuleChecker
from domain.node.person import Person
from domain.supportive.contract_error import ContractError


class RuleCheckerSpec(unittest.TestCase):

    def setUp(self):
        self.a_person = Person()
        self.rule_checker = RuleChecker()

    def it_checks_which_decorators_can_decorate_a_node(self):
        self.rule_checker.can_decorate(self.a_person)
        self.rule_checker.allowable_decorators |should| contain('Credit Analyst')

