import unittest
from should_dsl import should, should_not
#from ludibrio import Stub
from domain.node.person import Person
from domain.movement.process import Process
from domain.movement.transformation import Transformation
from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
from domain.supportive.association_error import AssociationError


class IndividualCreditOperationSpec(unittest.TestCase):

    def setUp(self):
        self.an_individual_credit_operation = Process()
        #test doubles won't work given type checking rules, using classic
        self.loan_request_creation = Transformation()
        #should create a person first and then decorate it, just for passing tests now
        self.a_credit_analyst_decorator = CreditAnalystDecorator('12345-6')

    def it_creates_a_loan_request(self):
        #method, but non @operation, should not associate
        self.loan_request_creation.set_operation(self.a_credit_analyst_decorator.change_loan_limit)
        self.loan_request_creation.operation |should| be(None)
        #@operation, should work
        self.loan_request_creation.set_operation(self.a_credit_analyst_decorator.create_loan_request)
        self.loan_request_creation.operation |should| equal_to(self.a_credit_analyst_decorator.create_loan_request)
        #associates the transformation to the process
        self.an_individual_credit_operation.insert_movement(self.loan_request_creation)
        self.an_individual_credit_operation.movements |should| contain(self.loan_request_creation)
        #finally it runs the transformation
        self.an_individual_credit_operation.movements[0].run('1234567-8', 10000)

