from datetime import datetime
from should_dsl import should
from domain.resource.material import Material
from domain.supportive.association_error import AssociationError
from domain.supportive.rule import rule
#from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
from bank_system.decorators.bank_account_decorator import BankAccountDecorator


class LoanRequest(Material):

    def __init__(self, account, value, analyst):
        Material.__init__(self)
        self.value = value
        self.approved = False
        self.datetime = datetime.now()
        self.analyst = analyst
        try:
           #self.rule_should_be_credit_analyst_instance(analyst) --> circular reference, how to solve?
           self.rule_should_be_bank_account_instance(account)
        except:
           raise AssociationError('Bank Account instance expected, instead %s passed' % type(account))
        else:
           self.account = account

    @rule('association')
    def rule_should_be_bank_account_instance(self, account):
        account |should| be_instance_of(BankAccountDecorator)

