import unittest
from should_dsl import should
import bank_system.decorators.credit_analyst_decorator
import bank_system.resources
from configurator.documenter import Documenter


class DocumenterSpec(unittest.TestCase):

    def setUp(self):
        self.documenter = Documenter()

    def it_finds_classes(self):
        #for bank_system.decorators should work like bank_system.resources...
        #a decorator module, which imports another decorator module
        self.documenter.find_classes(bank_system.decorators.credit_analyst_decorator)
        self.documenter |should| have(2).decorators
        #a resource module
        self.documenter.find_classes(bank_system.resources)
        self.documenter |should| have(2).resources

