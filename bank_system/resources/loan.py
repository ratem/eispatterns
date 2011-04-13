from datetime import datetime
from should_dsl import should
from domain.supportive.association_error import AssociationError
from domain.supportive.rule import rule
from domain.resource.material import Material
from bank_system.resources.loan_request import LoanRequest


class Loan(Material):
    ''' Loan generated from a Loan Request '''
    def __init__(self, loan_request):
        Material.__init__(self)
        try:
           self.rule_should_be_loan_request_instance(loan_request)
        except:
           raise AssociationError('Loan Request instance expected, instead %s passed' % type(loan_request))
        self.loan_request = loan_request
        self.datetime = datetime.now()

    @rule('association')
    def rule_should_be_loan_request_instance(self, loan_request):
        ''' Loan Request should be of type Loan Request '''
        loan_request |should| be_instance_of(LoanRequest)

