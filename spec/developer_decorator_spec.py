import unittest
from should_dsl import should, should_not
from domain.person import Person
from domain.developer_decorator import DeveloperDecorator


class DeveloperDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.a_developer_decorator = DeveloperDecorator()
        #test doubles won't work here, using classic
        self.a_person = Person()

    def it_checks_rules_of_association(self):
        #should work
        self.a_developer_decorator.decorate(self.a_person)
        self.a_developer_decorator.decorated |should| be(self.a_person)
        #should fail
        non_person = 'I am not a person'
        (self.a_developer_decorator.decorate, non_person) |should| throw(ValueError)

    def it_queries_rules_of_association(self):
        self.a_developer_decorator.query_rules_of_association() |should| start_with('decorated')

    def it_set_its_skills(self):
        self.a_developer_decorator.set_skills('Python','Junior','TDD, BDD')
        self.a_developer_decorator.language |should| be('Python')
        self.a_developer_decorator.level |should| be('Junior')
        self.a_developer_decorator.other_skills |should| be('TDD, BDD')

    def it_develops(self):
        self.a_developer_decorator.develop()
        self.a_developer_decorator |should| respond_to('source_code')

