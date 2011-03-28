from should_dsl import should
from domain.base.decorator import Decorator
from domain.node.person import Person
from domain.resource.operation import operation
from domain.supportive.rule import rule
from domain.supportive.association_error import AssociationError


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
    def create_loan_request(self, bank_account, value):
        return value

    #stupid credit analysis, only for demonstration
    @operation(category='business')
    def analyse(self, bank_account, value):
        if not bank_account.restricted:
            if bank_account.average_credit*4 > value:
                return True
            else:
                return False
        else:
            return False

    def change_loan_limit(self, new_limit):
        self.loan_limit = new_limit

