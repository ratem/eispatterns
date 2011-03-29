from should_dsl import should
from domain.base.decorator import Decorator
from domain.node.person import Person
from domain.resource.operation import operation
from domain.supportive.rule import rule
from domain.supportive.association_error import AssociationError
from bank_system.resources.loan_request import LoanRequest


class CreditAnalystDecorator(Decorator):

    def __init__(self, register):
        Decorator.__init__(self)
        self.description = "Some employee with credit analysis skills"
        self.register = register
        self.loan_limit = 0

    def decorate(self, decorated):
        try:
            self.rule_should_be_person_instance(decorated)
        except:
            raise AssociationError('Person instance expected, instead %s passed' % type(decorated))
        self.decorated = decorated

    @rule('association')
    def rule_should_be_person_instance(self, decorated):
        decorated |should| be_instance_of(Person)

    #creates a loan request
    @operation(category='business')
    def create_loan_request(self, account_number, value):
        loan_request = LoanRequest(account_number, value, self)
        #Sends the the loan_request for the input area
        loan_key = 'loan request %s'% account_number
        self.decorated.receive_resource(loan_key, loan_request)

    #stupid credit analysis, only for demonstration
    @operation(category='business')
    def analyse(self, loan_request):
        if not loan_request.account.restricted:
            if loan_request.account.average_credit*4 > loan_request.value:
                #waiting for creating moving methods in node
                return True
            else:
                return False
        else:
            return False

    def change_loan_limit(self, new_limit):
        self.loan_limit = new_limit

