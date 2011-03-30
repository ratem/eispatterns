import unittest
from should_dsl import should, should_not
from domain.node.person import Person
from domain.supportive.association_error import AssociationError
from bank_system.resources.loan_request import LoanRequest
from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
from bank_system.decorators.bank_account_decorator import BankAccountDecorator


class CreditAnalystDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.a_credit_analyst_decorator = CreditAnalystDecorator('12345-6')
        #test doubles won't work given type checking rules, using classic
        self.a_person = Person()
        self.an_account = BankAccountDecorator('1234567-8')

    def it_decorates_a_person(self):
        #should work
        self.a_credit_analyst_decorator.decorate(self.a_person)
        self.a_credit_analyst_decorator.decorated |should| be(self.a_person)
        #should fail
        non_person = 'I am not a person'
        (self.a_credit_analyst_decorator.decorate, non_person) |should| throw(AssociationError)

    def it_creates_a_loan_request(self):
        #tests ran out of order, thus forcing the decoration
        self.a_credit_analyst_decorator.decorate(self.a_person)
        self.a_credit_analyst_decorator.create_loan_request(self.an_account, 10000)
        self.a_person.input_area |should| contain('1234567-8')

    def it_analyses_a_loan_request(self):
        #Stub removed, now Node really transfers resources internally
        #tests ran out of order, do it all again
        self.a_credit_analyst_decorator.decorate(self.a_person)
        self.an_account.average_credit = 12500
        self.an_account.restricted = False
        self.a_credit_analyst_decorator.create_loan_request(self.an_account, 10000)
        #finally analyses de loan
        self.a_credit_analyst_decorator.analyse(self.an_account.number) |should| equal_to(True)

    def it_changes_its_loan_limit(self):
        self.a_credit_analyst_decorator.change_loan_limit(100000)
        self.a_credit_analyst_decorator.loan_limit |should| be(100000)

