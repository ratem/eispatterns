import unittest
from should_dsl import should, should_not
from ludibrio import Stub
from domain.node.person import Person
from domain.node.machine import Machine
from domain.supportive.association_error import AssociationError
from bank_system.resources.loan_request import LoanRequest
from bank_system.resources.loan import Loan
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
        self.a_credit_analyst_decorator.decorate(self.a_person)
        self.a_credit_analyst_decorator.create_loan_request(self.an_account, 10000)
        self.a_person.input_area |should| contain('1234567-8')

    def it_analyses_a_loan_request(self):
        #Stub removed, from now on Node really transfers resources internally
        self.a_credit_analyst_decorator.decorate(self.a_person)
        self.an_account.average_credit = 5000
        self.a_credit_analyst_decorator.create_loan_request(self.an_account, 10000)
        #analyses de loan
        self.a_credit_analyst_decorator.analyse(self.an_account.number) |should| equal_to(True)
        #just to check if the loan moved to the output_area
        self.a_person.output_area |should| contain('1234567-8')

    def it_creates_a_loan(self):
        loan_request = LoanRequest(self.an_account, 7000, self.a_credit_analyst_decorator)
        self.a_credit_analyst_decorator.decorate(self.a_person)
        self.a_credit_analyst_decorator.decorated.output_area[self.an_account.number] = loan_request
        #creates a machine to be decorated by the account - will need to check its processing_area
        a_machine = Machine()
        self.an_account.decorate(a_machine)
        #creates the loan
        self.a_credit_analyst_decorator.create_loan(loan_request)
        #the account's log_area should contain the loan request
        self.an_account.log_area |should| contain(loan_request.datetime)
        #the associated machine processing_area should contain the loan
        #since there is no way of acessing the recently created loan here:
        self.an_account.decorated.processing_area |should| have(1).loan

    def it_changes_its_loan_limit(self):
        self.a_credit_analyst_decorator.change_loan_limit(100000)
        self.a_credit_analyst_decorator.loan_limit |should| be(100000)

