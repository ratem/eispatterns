import unittest
from should_dsl import should
from domain.node.node import Node
from domain.movement.movement import Movement
from domain.movement.process import Process
from domain.resource.operation import operation
from domain.supportive.association_error import AssociationError


class FakeDecorator:
    @operation(category='anyone')
    def do_something(self, a_number, another_number):
        ''' I do something '''
        return a_number + another_number

class ProcessSpec(unittest.TestCase):

    def setUp(self):
        self.a_client = Node()
        self.the_company = Node()
        self.a_process = Process()
        self.a_process.set_source(self.the_company)
        self.a_process.set_destination(self.a_client)

    def it_inserts_a_movement(self):
        #should not work
        non_movement = "I am not a Movement"
        (self.a_process.insert_movement, 'Ops!',non_movement) |should| throw(AssociationError)
        #test doubles won't work given type checking rules
        a_movement = Movement()
        self.a_process.insert_movement('A movement', a_movement)
        self.a_process.movements |should| contain('A movement')

    def it_inserts_a_subprocess(self):
        a_subprocess = Process()
        self.a_process.insert_movement('A subprocess', a_subprocess)

    def an_activity(self):
        '''
        Represents an activity of a workflow engine.
        A business decorator's method will be attributed to this activity,
        making the activity a proxy to the decorator's method.
        '''
        pass

    def it_configures_a_movement_as_an_activity_logger(self):
        logger = self.a_process.configure_activity_logger(self.the_company, self.a_client, self.an_activity, FakeDecorator.do_something)
        logger.source |should| be(self.the_company)
        logger.destination |should| be(self.a_client)
        logger.activity |should| equal_to(self.an_activity)
        logger.activity_associated_method |should| equal_to(FakeDecorator.do_something)
        self.a_process.movements |should| include(self.an_activity.__name__)

    def it_runs_an_activity_through_a_preconfigured_activity_logger(self):
        logger = self.a_process.configure_activity_logger(self.the_company, self.a_client, self.an_activity, FakeDecorator.do_something)
        a_decorator = FakeDecorator()
        logger.context = self.a_process.run_activity(logger, a_decorator, 100, 200)
        logger.context['actor'] |should| be(a_decorator)
        logger.context['arguments'] |should| equal_to([100,200])
        logger.context['result'] |should| equal_to(300)

