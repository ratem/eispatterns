import unittest
from should_dsl import should
from domain.movement.process import Process
from domain.statemachine.configuration import ProcessTemplate


class CreditAnalyst(object):
    def create_loan(self): pass


class ProcessConfigurationSpec(unittest.TestCase):

    def it_configures_a_process(self):
        template = ProcessTemplate(initial_state='start')
        template.transformation('Create Loan', action=CreditAnalyst.create_loan)
        process = Process()
        process.configure(template)
        process |should| have(1).states
        process.states |should| include_all_of(['start'])
        process |should| have(1).transformations
        transformation = process.transformations[0]
        transformation.name |should| equal_to('Create Loan')
        transformation.action |should| equal_to(CreditAnalyst.create_loan)

