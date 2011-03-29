import unittest
from should_dsl import should, should_not
from ludibrio import Stub
from domain.node.person import Person
from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
from domain.supportive.association_error import AssociationError
from bank_system.resources.loan_request import LoanRequest

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
        #tests ran out of order, thus forcing the decoration
        self.a_credit_analyst_decorator.decorate(self.a_person)
        self.a_credit_analyst_decorator.create_loan_request('1234567-8', 10000)
        self.a_person.input_area |should| contain('loan request 1234567-8')

    def it_analyses_credit(self):
        with Stub() as loan_request:
            loan_request.account.restricted     >> False
            loan_request.account.average_credit >> 2500.00
            loan_request.value                  >> 5000
        self.a_credit_analyst_decorator.analyse(loan_request) |should| be(True)


    def it_changes_its_loan_limit(self):
        self.a_credit_analyst_decorator.change_loan_limit(100000)
        self.a_credit_analyst_decorator.loan_limit |should| be(100000)

