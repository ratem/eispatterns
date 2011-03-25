import unittest
from should_dsl import should, should_not
from ludibrio import Stub
from domain.node.person import Person
from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
from domain.supportive.association_error import AssociationError


class CreditAnalystDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.a_credit_analyst_decorator = CreditAnalystDecorator('12345-6')
        #test doubles won't work given type checking rules, using classic
        self.a_person = Person()

    def it_decorates_a_person(self):
        #should work
        self.a_credit_analyst_decorator.decorate(self.a_person)
        self.a_credit_analyst_decorator.decorated |should| be(self.a_person)
        #should fail
        non_person = 'I am not a person'
        (self.a_credit_analyst_decorator.decorate, non_person) |should| throw(AssociationError)

    def it_creates_a_loan_request(self):
        self.a_credit_analyst_decorator.create_loan_request('1234567-8', 10000) |should| be(10000)

    def it_analyses_credit(self):
        with Stub() as bank_account:
            bank_account.number           >> '12345-X'
            bank_account.average_credit   >> 2500.00
            bank_account.open_loans_total >> 12000.00
            bank_account.restricted       >> False
            bank_account.credit_limit     >> 20000.00
        self.a_credit_analyst_decorator.analyse(bank_account, 5000) |should| be(True)

    def it_changes_its_loan_limit(self):
        self.a_credit_analyst_decorator.change_loan_limit(100000)
        self.a_credit_analyst_decorator.loan_limit |should| be(100000)

