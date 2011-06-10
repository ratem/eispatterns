from should_dsl import should, ShouldNotSatisfied
from domain.base.decorator import Decorator
from domain.node.person import Person
from domain.node.node import Node
from domain.resource.operation import operation
from domain.supportive.rule import rule
from domain.supportive.association_error import AssociationError
from domain.supportive.contract_error import ContractError
from domain.supportive.contract_matchers import be_decorated_by
from bank_system.resources.loan_request import LoanRequest
from bank_system.resources.loan import Loan
from bank_system.decorators.bank_account_decorator import BankAccountDecorator
from bank_system.decorators.employee_decorator import EmployeeDecorator


class CreditAnalystDecorator(Decorator):
    '''Credit Analyst'''
    def __init__(self, register):
        Decorator.__init__(self)
        self.description = "An employee with credit analysis skills"
        self.register = register
        self.loan_limit = 0

    def decorate(self, decorated):
        try:
            CreditAnalystDecorator.rule_should_contain_employee_decorator(decorated)
        except:
            raise AssociationError('Person must be previously decorated by Employee Decorator')
        self.decorated = decorated
        self.decorated.decorators[self.__doc__] = self

    @classmethod
    @rule('association')
    def rule_should_contain_employee_decorator(self, decorated):
        ''' Decorated object should be already decorated by Employee '''
        decorated |should| be_decorated_by(EmployeeDecorator)

    #creates a loan request
    @operation(category='business')
    def create_loan_request(self, account, value):
        ''' creates a loan request '''
        loan_request = LoanRequest(account, value, self)
        #Puts the loan_request to the input area
        self.decorated.input_area[loan_request.account.number] = loan_request

    #stupid credit analysis, only for demonstration
    @operation(category='business')
    def analyse(self, loan_request_key):
        ''' automatically analyses a loan request '''
        if not self.decorated.input_area.has_key(loan_request_key): return False
        #move the request from the input_area to the processing_area
        self.decorated.transfer(loan_request_key,'input','processing')
        #picks the loan for processing
        loan_request = self.decorated.processing_area[loan_request_key]
        #automatically approves or not
        if not loan_request.account.restricted:
           if loan_request.account.average_credit*4 > loan_request.value:
               loan_request.approved = True
           else:
               loan_request.approved = False
        else:
           loan_request.approved = False
        #transfers the loan to the output_area
        self.decorated.transfer(loan_request_key,'processing','output')

    @operation(category='business')
    def create_loan(self, loan_request):
        ''' creates a loan '''
        loan = Loan(loan_request)
        #puts the new loan on the analyst's output_area, using analyst's register as key
        self.decorated.output_area[loan.loan_request.analyst.register] = loan

    @operation(category='business')
    def move_loan_to_account(self, loan_key, account):
        ''' moves the approved loan to the account '''
        try:
            loan = self.decorated.output_area[loan_key]
            loan |should| be_instance_of(Loan)
        except KeyError:
            raise KeyError("Loan with key %s not found in Analyst's output area" % loan_key)
        except ShouldNotSatisfied:
            raise ContractError('Loan instance expected, instead %s passed' % type(loan))
        try:
            Node.move_resource(loan_key, self.decorated, account.decorated)
        except ShouldNotSatisfied:
            raise ContractError('Bank Account instance expected, instead %s passed' % type(account))
        account.register_credit(loan.loan_request.value)

    def change_loan_limit(self, new_limit):
        self.loan_limit = new_limit

