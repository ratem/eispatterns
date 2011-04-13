import unittest
from should_dsl import should
import bank_system.decorators.credit_analyst_decorator
import bank_system.resources
from configurator.documenter import Documenter
import configurator.rule_checker_imports


class DocumenterSpec(unittest.TestCase):

    def setUp(self):
        self.documenter = Documenter()

    def it_finds_classes(self):
        #a decorator module, which imports another decorator module
        self.documenter.find_classes(bank_system.decorators.credit_analyst_decorator)
        self.documenter |should| have(2).decorators
        #a resource module
        self.documenter.find_classes(bank_system.resources.loan)
        self.documenter |should| have(2).resources
        #a imports module
        self.documenter.find_classes(configurator.rule_checker_imports)
        self.documenter |should| have(2).decorators
        self.documenter |should| have(2).resources

