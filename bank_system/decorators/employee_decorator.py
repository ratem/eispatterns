from should_dsl import should
from domain.base.decorator import Decorator
from domain.node.person import Person
from domain.resource.operation import operation
from domain.supportive.rule import rule
from domain.supportive.association_error import AssociationError


class EmployeeDecorator(Decorator):
    '''A general purpose Employee decorator'''
    def __init__(self):
        Decorator.__init__(self)
        self.description = "Supplies the basis for representing employes"

    def generate_register(self, register):
        ''' generates the register number for the employee '''
        self.register = register

    def decorate(self, decorated):
        try:
            EmployeeDecorator.rule_should_be_person_instance(decorated)
        except:
            raise AssociationError('Person instance expected, instead %s passed' % type(decorated))
        self.decorated = decorated
        self.decorated.decorators[self.__doc__] = self

    @classmethod
    @rule('association')
    def rule_should_be_person_instance(self, decorated):
        ''' Decorated object should be a Person '''
        decorated |should| be_instance_of(Person)

