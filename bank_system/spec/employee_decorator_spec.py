import unittest
from should_dsl import should
from domain.node.person import Person
from domain.supportive.association_error import AssociationError
from bank_system.decorators.employee_decorator import EmployeeDecorator


class EmployeeDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.an_employee_decorator = EmployeeDecorator()
        #test doubles won't work given type checking rules, using classic
        self.a_person = Person()

    def it_decorates_a_person(self):
        #should work
        self.an_employee_decorator.decorate(self.a_person)
        self.an_employee_decorator.decorated |should| be(self.a_person)
        self.an_employee_decorator.decorated |should| have(1).decorators
        #should fail
        non_person = 'I am not a person'
        (self.an_employee_decorator.decorate, non_person) |should| throw(AssociationError)

    def it_generates_register(self):
        self.an_employee_decorator.generate_register('123456-7')
        self.an_employee_decorator.register |should| equal_to('123456-7')

