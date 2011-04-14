from should_dsl import should
from domain.base.decorator import Decorator
from domain.node.machine import Machine
from domain.resource.operation import operation
from domain.supportive.rule import rule
from domain.supportive.association_error import AssociationError


class BankAccountDecorator(Decorator):
    '''Bank Account'''
    def __init__(self, number):
        Decorator.__init__(self)
        self.description = "A bank account"
        #log area for already processed resources
        self.log_area = {}
        #should it mask Machine.tag? decorated.tag = number?
        self.number = number
        self.restricted = False
        self.average_credit = 0

    def decorate(self, decorated):
        try:
            BankAccountDecorator.rule_should_be_machine_instance(decorated)
        except:
            raise AssociationError('Machine instance expected, instead %s passed' % type(decorated))
        self.decorated = decorated
        self.decorated.decorators[self.__doc__] = self

    @classmethod
    @rule('association')
    def rule_should_be_machine_instance(self, decorated):
        ''' Decorated object should be a Machine '''
        decorated |should| be_instance_of(Machine)

