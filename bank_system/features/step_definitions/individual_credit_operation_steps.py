# -*- coding: utf-8 -*-
from lettuce import step, world
from should_dsl import should
from domain.node.person import Person
from domain.node.machine import Machine
from domain.movement.process import Process
from domain.movement.transformation import Transformation
from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
from bank_system.decorators.bank_account_decorator import BankAccountDecorator

#Scenario Individual Customer asks for loan
@step(u'Given I am a registered Credit Analyst')
def given_i_am_a_registered_credit_analyst(step):
    world.a_person = Person()
    world.credit_analyst = CreditAnalystDecorator('09876-5')
    world.credit_analyst.decorate(world.a_person)

@step(u'And an individual customer with account number (.+) asks for a personal loan')
def and_an_individual_customer_with_account_number_account_number_asks_for_a_personal_loan(step, account_number):
    world.a_machine = Machine()
    world.account = BankAccountDecorator(account_number)
    world.account.decorate(world.a_machine)

@step(u'And the loan request is of (.+)')
def and_the_loan_request_is_of_desired_value(step, desired_value):
    #GUI action
    pass

@step(u'When I confirm the loan request')
def when_i_confirm_the_loan_request(step):
    #GUI action
    pass

@step(u'Then a new loan request with the (.+) and (.+) is created')
def then_a_new_loan_request_with_the_account_number_and_desired_value_is_created(step, account_number, desired_value):
    #now the business process starts to be assembled
    world.an_individual_credit_operation = Process()
    world.loan_request_creation = Transformation()
    world.loan_request_creation.set_operation(world.credit_analyst.create_loan_request)
    world.loan_request_creation.operation |should| equal_to(world.credit_analyst.create_loan_request)
    #associates the transformation to the process
    world.an_individual_credit_operation.insert_movement(world.loan_request_creation)
    world.an_individual_credit_operation.movements |should| contain(world.loan_request_creation)
    #finally it runs the transformation...
    world.an_individual_credit_operation.movements[0].run(world.account, desired_value)
    #checks if the loan request is stored in the Node's input_area
    world.a_person.input_area |should| contain(account_number)

@step(u'And the new loan request is associated to the Credit Analyst')
def and_the_new_loan_request_is_associated_to_the_credit_analyst(step):
    #... the association is done during loan creation, just checking
    world.a_person.input_area[world.account.number].analyst |should| be(world.credit_analyst)

#Scenario Credit Analyst analyses the individual customer loan request
@step(u'And there is a loan request of account (.+) to be analysed')
def and_there_is_a_loan_request_of_account_account_number_to_be_analysed(step, account_number):
    #Letucce cleans the objects of the previous scenario, thus creating loan request again
    #Could do this, however, it contains stuff that I need here
    #step.then('a new loan request with the %s and %f is created' % (account_number, 10000))
    #Thus...
    #world.a_person.input_area = {}
    world.credit_analyst.decorate(world.a_person)
    world.credit_analyst.create_loan_request(world.account, 10000)
    world.a_person.input_area |should| contain(world.account.number)

@step(u'When I pick the loan request of account (.+) and analyse it')
def when_i_pick_the_loan_request_of_account_account_number_and_analyse_it(step, account_number):
    #creates a new transformation to register the analysis
    world.loan_request_analysis = Transformation()
    #associates analyse operation to the transformation
    world.loan_request_analysis.set_operation(world.credit_analyst.analyse)
    #associates the transformation to the process
    world.an_individual_credit_operation.insert_movement(world.loan_request_analysis)
    #finally it runs the transformation...
    #must refactor process.movements to make it easier to find operations => use a dictionary
       #strange - analyse doesn't work in this context, even when it is directly called
    world.an_individual_credit_operation.movements[1].run(world.account.number)
    #if everything is ok the loan request was stored in the Node's output_area
    #world.a_person.processing_area |should| contain(account_number)

@step(u'Then The loan request enters the state ANALYSED with decision <decision>')
def then_the_loan_request_enters_the_state_analysed_with_decision_decision(step):
    pass

