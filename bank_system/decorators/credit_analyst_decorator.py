from inspect import getsource
from should_dsl import should
from domain.base.decorator import Decorator
from domain.node.person import Person


class CreditAnalystDecorator(Decorator):

    def __init__(self, register):
        Decorator.__init__(self)
        self.description = "Some employee with credit analysis skills"
        self.register = register
        self.loan_limit = 0

    def decorate(self, decorated):
        try:
            self.rule_should_be_person_instance(decorated)
        except: #need a customized exception here
            raise ValueError('Person instance expected, instead %s passed' % type(decorated))
        self.decorated = decorated

    def query_rules_of_association(self,query=None):
        '''rule_method = getsource(self.rule_should_be_person_instance)
        #very stupid code downwards
        #splits after the method signature
        rule_method_code = rule_method.split('\n')
        #strip the method signature
        rule_method_code = rule_method_code[1]
        #strip whitespaces
        rule_method_code = rule_method_code.lstrip(' ')
        return rule_method_code
        '''
        pass

    def rule_should_be_person_instance(self, decorated):
        decorated |should| be_instance_of(Person)

    def change_loan_limit(self, new_limit):
        self.loan_limit = new_limit

    #stupid code downwards, should be:
    #resource/operation/credit_analysis object in use
    #movement/transformation realizes the credit_analysis on a resource/material/credit_document
    #as part of a movement/process => process is the coordinator object
    def analyse(self, account):
        return True

