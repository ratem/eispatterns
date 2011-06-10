import unittest
from should_dsl import should, should_not
from domain.node.person import Person
from domain.node.machine import Machine
from domain.supportive.association_error import AssociationError
from domain.supportive.contract_error import ContractError
from bank_system.resources.loan_request import LoanRequest
from bank_system.resources.loan import Loan
from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
from bank_system.decorators.bank_account_decorator import BankAccountDecorator
from bank_system.decorators.employee_decorator import EmployeeDecorator


class CreditAnalystDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.a_credit_analyst_decorator = CreditAnalystDecorator('12345-6')
        #test doubles won't work given type checking rules, using classic
        self.a_person = Person()
        self.an_account = BankAccountDecorator('1234567-8')

    def it_decorates_a_person(self):
        #should fail
        (self.a_credit_analyst_decorator.decorate, self.a_person) |should| throw(AssociationError)
        #should work
        an_employee_decorator = EmployeeDecorator()
        an_employee_decorator.decorate(self.a_person)
        self.a_credit_analyst_decorator.decorate(self.a_person)
        self.a_credit_analyst_decorator.decorated |should| be(self.a_person)
        self.a_credit_analyst_decorator.decorated |should| have(2).decorators

    def it_creates_a_loan_request(self):
        an_employee_decorator = EmployeeDecorator()
        an_employee_decorator.decorate(self.a_person)
        self.a_credit_analyst_decorator.decorate(self.a_person)
        self.a_credit_analyst_decorator.create_loan_request(self.an_account, 10000)
        self.a_person.input_area |should| contain('1234567-8')

    def it_analyses_a_loan_request(self):
        an_employee_decorator = EmployeeDecorator()
        an_employee_decorator.decorate(self.a_person)
        #Stub removed, from now on Node really transfers resources internally
        self.a_credit_analyst_decorator.decorate(self.a_person)
        self.an_account.average_credit = 5000
        #should approve
        self.a_credit_analyst_decorator.create_loan_request(self.an_account, 10000)
        self.a_credit_analyst_decorator.analyse(self.an_account.number)
        self.a_credit_analyst_decorator.decorated.output_area['1234567-8'].approved |should| equal_to(True)
        #should refuse
        self.a_credit_analyst_decorator.create_loan_request(self.an_account, 50000)
        self.a_credit_analyst_decorator.analyse(self.an_account.number)
        self.a_credit_analyst_decorator.decorated.output_area['1234567-8'].approved |should| equal_to(False)

    def it_creates_a_loan(self):
        an_employee_decorator = EmployeeDecorator()
        an_employee_decorator.decorate(self.a_person)
        loan_request = LoanRequest(self.an_account, 7000, self.a_credit_analyst_decorator)
        self.a_credit_analyst_decorator.decorate(self.a_person)
        self.a_credit_analyst_decorator.decorated.output_area[self.an_account.number] = loan_request
        #creates a machine to be decorated by the account - will need to check its processing_area
        a_machine = Machine()
        self.an_account.decorate(a_machine)
        #creates the loan
        self.a_credit_analyst_decorator.create_loan(loan_request)
        #loan key is the analyst's register
        self.a_credit_analyst_decorator.decorated.output_area.values() |should| have_at_least(1).loan
        self.a_credit_analyst_decorator.decorated.output_area |should| include(self.a_credit_analyst_decorator.register)

    def it_moves_the_loan_to_an_account(self):
        #prepares the person Node
        an_employee_decorator = EmployeeDecorator()
        an_employee_decorator.decorate(self.a_person)
        self.a_credit_analyst_decorator.decorate(self.a_person)
        #prepares a Loan
        loan_request = LoanRequest(self.an_account, 7000, self.a_credit_analyst_decorator)
        self.a_credit_analyst_decorator.decorated.output_area[self.an_account.number] = loan_request
        self.a_credit_analyst_decorator.create_loan(loan_request)
        #should go wrong
        passing_a_wrong_key = 'wrong key'
        (self.a_credit_analyst_decorator.move_loan_to_account, passing_a_wrong_key, self.an_account) |should| throw(KeyError)
        passing_a_non_account = 'I am not an account'
        (self.a_credit_analyst_decorator.move_loan_to_account, self.an_account.number, passing_a_non_account) |should| throw(ContractError)
        #prepares the account
        a_machine = Machine()
        self.an_account.decorate(a_machine)
        #should work
        loan_key = self.a_credit_analyst_decorator.register
        self.a_credit_analyst_decorator.move_loan_to_account(loan_key, self.an_account)
        self.an_account.decorated.input_area |should| include(loan_key)

    def it_changes_its_loan_limit(self):
        self.a_credit_analyst_decorator.change_loan_limit(100000)
        self.a_credit_analyst_decorator.loan_limit |should| be(100000)

