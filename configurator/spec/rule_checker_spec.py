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
        #it works with configurator.import_decorators, a *import* module
        self.rule_checker.find_decorators(configurator.import_decorators)
        self.rule_checker.decorators |should| have(2).items

    def test_it_finds_decorators_rules(self):
        self.rule_checker.find_decorators(configurator.import_decorators)
        for decorator in self.rule_checker.decorators:
            self.rule_checker.find_rules(decorator)
        self.rule_checker.rules |should| have(2).rules

    def test_it_check_rules(self):
        self.rule_checker.find_decorators(configurator.import_decorators)
        for decorator in self.rule_checker.decorators:
            self.rule_checker.find_rules(decorator)
        self.rule_checker.check_rules(self.a_person)
        self.rule_checker.allowable_decorators |should| have(1).decorator
        #non_allowable should contain tuples (class, reason), where reason is
        #the __doc__ of a @rule == fine grained reasons for not decorating!

'''
if __name__ == '__main__':
    unittest.main()
'''

