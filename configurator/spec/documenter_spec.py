import unittest
from should_dsl import should
import bank_system.decorators.credit_analyst_decorator
import bank_system.resources
from configurator.documenter import Documenter
import configurator.rule_checker_imports
import configurator.documenter_imports

class DocumenterSpec(unittest.TestCase):

    def setUp(self):
        self.documenter = Documenter()

    def it_finds_classes(self):
        #a decorator module, which imports two other decorator modules
        self.documenter.find_classes(bank_system.decorators.credit_analyst_decorator)
        self.documenter |should| have(3).decorators
        #a resource module
        self.documenter.find_classes(bank_system.resources.loan)
        self.documenter |should| have(2).work_items
        #a imports module
        self.documenter.find_classes(configurator.rule_checker_imports)
        self.documenter |should| have(3).decorators
        self.documenter |should| have(2).work_items

    def it_lists_decorators_operations(self):
        self.documenter.find_classes(configurator.documenter_imports)
        self.documenter.list_decorators_operations()
        self.documenter |should| have(3).operations

    def it_lists_work_items_documentations(self):
        self.documenter.find_classes(configurator.documenter_imports)
        self.documenter.list_work_items_documentations()
        self.documenter |should| have(2).work_items_documentations

