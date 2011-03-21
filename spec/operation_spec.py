import unittest
from should_dsl import should
from domain.resource.operation import operation
from domain.node.person import Person

class OperationSpec(unittest.TestCase):

    def setUp(self):
        #@operator was created to typify Node/Person and Node/Machine business
        #decorators methods, however, its used directly on a person object here
        #to make it easier to understand its use.
        self.a_person = Person()

    @operation(category='skill')
    def something_a_person_can_do(self):
        something = 1
        something += 1
        return something

    def it_decorates_a_method(self):
        self.a_person.new_skill = self.something_a_person_can_do
        #the should below simultaneously demonstrates that the decorator
        #@operation works as well as it makes methods' "types" queriable
        self.a_person.new_skill.category |should| be('skill')

