''' Applying Fluidity & Extreme Fluidity to Process '''
import unittest
from should_dsl import should
from fluidity.machine import StateMachine, state, transition, InvalidTransition
from xfluidity import StateMachineConfigurator
from domain.node.node import Node
from domain.movement.process import Process
from domain.resource.operation import operation


class FakeDecorator:
    @operation(category='anyone')
    def do_something(self, number):
        ''' I do something '''
        return "this is an operation's return value:%s" % number

class LoanProcess(StateMachine):
    state('requested')
    state('request_created')
    state('request_analyzed')
    state('refusal_letter_sent')
    state('loan_created')
    state('value_transfered')
    initial_state = 'requested'
    transition(from_='requested', event='create_loan_request', to='request_created')
    transition(from_='request_created', event='analyst_select_request', to='request_analyzed')
    transition(from_='request_analyzed', event='loan_refused', to='refusal_letter_sent')
    transition(from_='request_analyzed', event='loan_accepted', to='loan_created')
    transition(from_='loan_created', event='time_to_transfer_value', to='value_transfered')

class FluidityProcessSpec(unittest.TestCase):

    def setUp(self):
        self.process = Process()
        template = LoanProcess()
        configurator = StateMachineConfigurator(template)
        configurator.configure(self.process)

    def it_makes_the_process_respond_to_the_example_state_machine_events(self):
        self.process |should| respond_to('create_loan_request')
        self.process |should| respond_to('analyst_select_request')
        self.process |should| respond_to('loan_refused')
        self.process |should| respond_to('loan_accepted')
        self.process |should| respond_to('time_to_transfer_value')

    def it_runs_the_example_refusal_path(self):
        self.process.create_loan_request()
        self.process.current_state() |should| equal_to('request_created')
        self.process.loan_refused |should| throw(InvalidTransition)
        self.process.analyst_select_request()
        self.process.current_state() |should| equal_to('request_analyzed')
        #loan refused
        self.process.loan_refused()
        self.process.current_state() |should| equal_to('refusal_letter_sent')

    def it_runs_the_example_acceptance_path(self):
        #process was restarted by setUp()
        self.process.create_loan_request()
        self.process.current_state() |should| equal_to('request_created')
        self.process.loan_refused |should| throw(InvalidTransition)
        self.process.analyst_select_request()
        self.process.current_state() |should| equal_to('request_analyzed')
        #loan accepted
        self.process.loan_accepted()
        self.process.current_state() |should| equal_to('loan_created')
        self.process.time_to_transfer_value()
        self.process.current_state() |should| equal_to('value_transfered')

    def it_configures_and_runs_a_process(self):
        self.a_node = Node()
        self.another_node = Node()
        self.a_decorator = FakeDecorator()
        #process was restarted by setUp()
        the_movement = self.process.configure_activity_logger(self.a_node, self.another_node, self.process.create_loan_request, FakeDecorator.do_something)
        #starts running
        the_movement.context = self.process.run_activity(the_movement, self.a_decorator, 10)
        the_movement.context['result'] |should| equal_to("this is an operation's return value:10")
        self.process.current_state() |should| equal_to('request_created')
        #configures and runs the template's refusal path
            #should go wrong
        the_movement = self.process.configure_activity_logger(self.a_node, self.another_node, self.process.loan_refused, FakeDecorator.do_something)
        (self.process.run_activity, the_movement, self.a_decorator, 10) |should| throw(InvalidTransition)
            #now doing the right thing
        the_movement = self.process.configure_activity_logger(self.a_node, self.another_node, self.process.analyst_select_request, FakeDecorator.do_something)
        the_movement.context = self.process.run_activity(the_movement, self.a_decorator,10)
        self.process.current_state() |should| equal_to('request_analyzed')
        the_movement = self.process.configure_activity_logger(self.a_node, self.another_node, self.process.loan_refused, FakeDecorator.do_something)
        the_movement.context = self.process.run_activity(the_movement, self.a_decorator,15)
        self.process.current_state() |should| equal_to('refusal_letter_sent')

