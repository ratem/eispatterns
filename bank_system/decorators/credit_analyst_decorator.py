from should_dsl import should
from domain.base.decorator import Decorator
from domain.node.person import Person
from domain.resource.operation import operation
from domain.supportive.rule import rule
from domain.supportive.association_error import AssociationError
from bank_system.resources.loan_request import LoanRequest
from bank_system.resources.loan import Loan
from bank_system.decorators.bank_account_decorator import BankAccountDecorator


class CreditAnalystDecorator(Decorator):
    '''Credit Analyst'''
    def __init__(self, register):
        Decorator.__init__(self)
        self.description = "An employee with credit analysis skills"
        self.register = register
        self.loan_limit = 0

    def decorate(self, decorated):
        try:
            CreditAnalystDecorator.rule_should_be_person_instance(decorated)
        except:
            raise AssociationError('Person instance expected, instead %s passed' % type(decorated))
        self.decorated = decorated

    @classmethod
    @rule('association')
    def rule_should_be_person_instance(self, decorated):
        decorated |should| be_instance_of(Person)

    #creates a loan request
    @operation(category='business')
    def create_loan_request(self, account, value):
        ''' creates a loan request '''
        loan_request = LoanRequest(account, value, self)
        #Puts the loan_request to the input area
        self.decorated.receive_resource(loan_request.account.number, loan_request)

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
        #puts the new loan on the analyst's output_area
        self.decorated.output_area[loan.datetime] = loan

    def change_loan_limit(self, new_limit):
        self.loan_limit = new_limit

