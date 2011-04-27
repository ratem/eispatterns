import unittest
from should_dsl import should
from domain.node.person import Person
from domain.movement.transformation import Transformation
from domain.resource.operation import operation

class Analyst:
    def analyze(self): pass


class TransformationSpec(unittest.TestCase):

    def setUp(self):
        self.a_person = Person()
        self.a_transformation = Transformation('A transformation',
            from_state='start', to_state='created', action=Analyst.analyze)
        self.a_transformation.set_source(self.a_person)
        self.a_transformation.set_destination(self.a_person)

    @operation(category='business')
    def an_operation(self, argument):
        ''' operations must be documented'''
        return argument

    def non_operation(self):
        return 0

    def it_sets_its_action(self):
        #should not work
        self.a_transformation.set_action(self.non_operation) |should| be(False)
        #should work
        self.a_transformation.set_action(self.an_operation)
        self.a_transformation.action |should| equal_to(self.an_operation)

    def it_stores_creation_attributes(self):
        a_transformation = Transformation('A transformation',
            from_state='started', to_state='created', action=Analyst.analyze)
        a_transformation.name |should| equal_to('A transformation')
        a_transformation.action |should| equal_to(Analyst.analyze)
        a_transformation.from_state |should| equal_to('started')
        a_transformation.to_state |should| equal_to('created')

    def it_performs(self):
        self.a_transformation.set_action(self.an_operation)
        self.a_transformation.perform(10)

