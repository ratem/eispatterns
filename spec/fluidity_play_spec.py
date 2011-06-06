import unittest
from should_dsl import should
from fluidity.machine import StateMachine, state, transition, InvalidTransition
from extreme_fluidity.xfluidity import StateMachineConfigurator
from domain.movement.process import Process
from domain.node.node import Node
from domain.resource.operation import operation


class FakeDecorator:
    def __main__(self):
        return 0

    @operation(category='anyone')
    def do_something(self, number):
        ''' I do something '''
        return 100*number

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

class StateMachineConfiguratorSpec(unittest.TestCase):

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
        #it is necessary to rebuild the path - need a calve_machine here or a reset()
        self.process = Process()
        template = LoanProcess()
        configurator = StateMachineConfigurator(template)
        configurator.configure(self.process)
        #restart the path
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

    def it_configures_a_transition(self):
        #arguments
        self.process = Process()
        self.a_node = Node()
        self.another_node = Node()
        self.a_decorator = FakeDecorator()
        #configuring the process
        configurator = StateMachineConfigurator(LoanProcess())
        configurator.configure(self.process)
        #configuring the first transition
        the_movement = self.process.configure_activity(self.a_node, self.another_node, self.process.create_loan_request, FakeDecorator.do_something)
        the_movement.activity_runner |should| equal_to(FakeDecorator.do_something)
        #running the first transition
        the_movement.result, the_movement.activity_start, the_movement.activity_end = self.process.run_activity(the_movement, self.a_decorator, 2)
        the_movement.result |should| equal_to(200)
        self.process.current_state() |should| equal_to('request_created')
        #configures and runs the refusal path: check Fluidity + Movement configuration

         #should go wrong
         #the_movement = self.process.configure_activity(self.a_node, self.another_node, self.process.loan_refused, FakeDecorator.do_something)
         #it goes wrong and returns the correct exception, however, I cannot catch it
         #self.process.run_activity(the_movement, self.a_decorator, 2) |should| throw(InvalidTransition)

        #now doing the right thing
        the_movement = self.process.configure_activity(self.a_node, self.another_node, self.process.analyst_select_request, FakeDecorator.do_something)
        the_movement.result, the_movement.activity_start, the_movement.activity_end = self.process.run_activity(the_movement, self.a_decorator, 2)
        self.process.current_state() |should| equal_to('request_analyzed')
        #loan refused
        the_movement = self.process.configure_activity(self.a_node, self.another_node, self.process.loan_refused, FakeDecorator.do_something)
        the_movement.result, the_movement.activity_start, the_movement.activity_end = self.process.run_activity(the_movement, self.a_decorator, 2)
        self.process.current_state() |should| equal_to('refusal_letter_sent')

