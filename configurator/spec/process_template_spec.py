import unittest
from should_dsl import should
from domain.movement.process import Process
from configurator.statemachine.process_templates import ProcessTemplate, StateMachineTemplate


class CreditAnalyst(object):
    def create_loan_request(self): pass
    def analyse_loan_request(self): pass
    def create_loan(self): pass
    def send_refusal_message(self): pass
    def transfer_value(self): pass


class ProcessConfigurationSpec(unittest.TestCase):

    def it_configures_a_process(self):
        template = ProcessTemplate(initial_state='start')
        template.transformation('Create Loan Request', action=CreditAnalyst.create_loan_request)
        process = Process()
        process.configure(template)
        process |should| have(1).states
        process.states |should| include_all_of(['start'])
        process |should| have(1).transformations
        transformation = process.transformations[0]
        transformation.name |should| equal_to('Create Loan Request')
        transformation.action |should| equal_to(CreditAnalyst.create_loan_request)

class StateMachineTemplateSpec(unittest.TestCase):

    def it_configures_a_process_as_a_state_machine(self):
        template = StateMachineTemplate()
        template.add_complete_transition('start', 'create loan request', 'loan request created')
        template.add_complete_transition('loan request created', 'analyse loan request', 'loan request analysed')
        template.add_complete_transition('loan request analysed', 'create loan', 'loan created')
        template.add_complete_transition('loan created', 'transfer value to account', 'loan transfered')
        template.add_complete_transition('loan request analysed','send refusal message', 'refusal message sent')

        template.associate_transition_to_movement('create loan request', CreditAnalyst.create_loan_request)
        template.associate_transition_to_movement('analyse loan request', CreditAnalyst.analyse_loan_request)
        template.associate_transition_to_movement('create loan', CreditAnalyst.create_loan)
        template.associate_transition_to_movement('transfer value to account', CreditAnalyst.transfer_value)
        template.associate_transition_to_movement('send refusal message', CreditAnalyst.send_refusal_message)

