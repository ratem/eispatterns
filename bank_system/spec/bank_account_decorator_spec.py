import unittest
from should_dsl import should, should_not
from domain.node.machine import Machine
from bank_system.decorators.bank_account_decorator import BankAccountDecorator
from domain.supportive.association_error import AssociationError


class bankAccountDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.a_bank_account_decorator = BankAccountDecorator('12345-6')
        #test doubles won't work given type checking rules, using classic
        self.a_machine = Machine()

    def it_decorates_a_machine(self):
        #should work
        self.a_bank_account_decorator.decorate(self.a_machine)
        self.a_bank_account_decorator.decorated |should| be(self.a_machine)
        #should fail
        non_machine = 'I am not a machine'
        (self.a_bank_account_decorator.decorate, non_machine) |should| throw(AssociationError)

