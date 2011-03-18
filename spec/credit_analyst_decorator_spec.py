import unittest
from should_dsl import should, should_not
from domain.node.person import Person
from domain.credit_analyst_decorator import CreditAnalystDecorator


class CreditAnalystDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.a_credit_analyst_decorator = CreditAnalystDecorator('12345-6')
        #test doubles won't work here, using classic
        self.a_person = Person()

    def it_decorates_a_person(self):
        #should work
        self.a_credit_analyst_decorator.decorate(self.a_person)
        self.a_credit_analyst_decorator.decorated |should| be(self.a_person)
        #should fail
        non_person = 'I am not a person'
        (self.a_credit_analyst_decorator.decorate, non_person) |should| throw(ValueError)

    def it_queries_rules_of_association(self):
        self.a_credit_analyst_decorator.query_rules_of_association() |should| start_with('decorated')

    def it_changes_its_loan_limit(self):
        self.a_credit_analyst_decorator.change_loan_limit(100000)
        self.a_credit_analyst_decorator.loan_limit |should| be(100000)

    def it_analyses_credit(self):
        self.a_credit_analyst_decorator.analyse('00001-12') |should| be(True)

