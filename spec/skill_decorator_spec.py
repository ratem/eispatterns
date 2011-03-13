import unittest
from should_dsl import should, should_not
from domain.immaterial import Immaterial
from domain.skill_decorator import SkillDecorator


class SkillDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.a_skill_decorator = SkillDecorator()
        #test doubles won't work here, using classic
        self.an_immaterial = Immaterial()

    def it_checks_rules_of_association(self):
        #should work
        (self.a_skill_decorator.check_rules_of_association,self.an_immaterial) |should_not| throw(ValueError)
        #should fail
        non_immaterial = 'I am not an immaterial'
        (self.a_skill_decorator.check_rules_of_association, non_immaterial) |should| throw(ValueError)

    def it_queries_rules_of_association(self):
        self.a_skill_decorator.query_rules_of_association('nop') |should| start_with('decorated')

