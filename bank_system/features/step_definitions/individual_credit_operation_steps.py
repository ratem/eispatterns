# -*- coding: utf-8 -*-
from lettuce import step, world
from should_dsl import should
from domain.node.person import Person
from domain.node.machine import Machine
from domain.movement.process import Process
from domain.movement.transformation import Transformation
from domain.movement.transportation import Transportation
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
    #Processes are nodes that use the company as the source node, and the client as destination
    world.the_company = Machine()
    world.a_client = Person()
    #now the business process starts to be assembled
    world.an_individual_credit_operation = Process(world.the_company, world.a_client)
    world.loan_request_creation = Transformation(world.credit_analyst.decorated, world.credit_analyst.decorated)
    world.loan_request_creation.set_action(world.credit_analyst.create_loan_request)
    world.loan_request_creation.action |should| equal_to(world.credit_analyst.create_loan_request)
    #associates the transformation to the process
    world.an_individual_credit_operation.insert_movement('loan request creation', world.loan_request_creation)
    world.an_individual_credit_operation.movements |should| contain('loan request creation')
    #finally it runs the transformation...
    world.an_individual_credit_operation.movements['loan request creation'].perform(world.account, desired_value)
    #checks if the loan request is stored in the Node's input_area
    world.a_person.input_area |should| contain(account_number)

@step(u'And the new loan request is associated to the Credit Analyst')
def and_the_new_loan_request_is_associated_to_the_credit_analyst(step):
    #... the association is done during loan creation, just checking
    world.a_person.input_area[world.account.number].analyst |should| be(world.credit_analyst)

#Scenario Credit Analyst analyses the individual customer loan request
@step(u'And there is a loan request of account (.+) to be analysed')
def and_there_is_a_loan_request_of_account_account_number_to_be_analysed(step, account_number):
    #Could do this, however, it contains stuff that I don't need here
    #step.then('a new loan request with the %s and %f is created' % (account_number, 10000))
    #Thus...
    world.credit_analyst.decorate(world.a_person)
    world.credit_analyst.create_loan_request(world.account, 10000)
    world.credit_analyst.decorated.input_area |should| contain(world.account.number)

@step(u'When I pick to analyse the loan request of account (.+)')
def when_i_pick_to_analyse_the_loan_request_of_account_account_number(step, account_number):
    #creates a new transformation to register the analysis
    world.loan_request_analysis = Transformation(world.credit_analyst.decorated, world.credit_analyst.decorated)
    #associates analyse operation to the transformation
    world.loan_request_analysis.set_action(world.credit_analyst.analyse)
    #associates the transformation to the process
    world.an_individual_credit_operation.insert_movement('loan request analysis', world.loan_request_analysis)
    #finally it runs the transformation...
    #must refactor process.movements to make it easier to find operations => use a dictionary
    world.an_individual_credit_operation.movements['loan request analysis'].perform(world.account.number)
    #if everything is ok the loan request was stored in the Node's output_area
    world.a_person.output_area |should| contain(account_number)

@step(u'Then the loan request has the decision (.+)')
def then_the_loan_request_has_the_decision_decision(step, decision):
    #Lettuce sends u'False', thus using eval() to convert in into boolean
    world.credit_analyst.decorated.output_area['1234567-8'].approved |should| equal_to(eval(decision))

#Scenario Approved loan request
@step(u'Given a loan request of value (.+) for account (.+) was approved')
def given_a_loan_request_of_value_value_for_account_account_number_was_approved(step, value, account_number):
    #directly creating a loan request (I really need BLDD to avoid this...)
    world.credit_analyst.create_loan_request(world.account, value)
    #forces the loan request approval
    world.credit_analyst.decorated.input_area[world.account.number].approved = True
    world.credit_analyst.decorated.input_area |should| contain(world.account.number)

@step(u'When I pick and perfom this loan')
def when_i_pick_and_perfom_this_loan(step):
    #picking...
    loan_request = world.credit_analyst.decorated.input_area[world.account.number]
    #preparing to perform...
    world.create_loan = Transformation(world.credit_analyst.decorated, world.credit_analyst.decorated)
    world.create_loan.set_action(world.credit_analyst.create_loan)
    world.an_individual_credit_operation.insert_movement('loan creation', world.create_loan)
    #performing!
    world.an_individual_credit_operation.movements['loan creation'].perform(loan_request)
    #given that I am using datetime to generate the key, I cannot access the newly
    #created loan through its key
    #output_area must have at least the loan_request and the newly created loan
    world.credit_analyst.decorated.output_area.values() |should| have_at_least(2).itens

@step(u'Then a loan of value (.+) for account (.+) is generated')
def then_a_loan_of_value_value_for_account_account_number_is_generated(step, value, account_number):
    #moves the loan to the processing area of the account
    world.move_loan_to_account = Transportation(world.credit_analyst.decorated, world.account.decorated)
    #world.move_loan_to_account.transport(??? how to get the new loan key ???)
    #world.account.decorated.transfer('input', 'processing')

@step(u'And the loan_request is moved to the account (.+) historic')
def and_the_loan_request_is_moved_to_the_account_account_number_historic(step, account_number):
    #moves the loan_request to the log_area of the account
    #be aware that there must be a movement and a transfer to the log_area

    #world.move_loan_to_account.transport(??? how to get the new loan key ???)
    #world.account.decorated.transfer(input, log) - ops!, no transfering to the log area
    #should all nodes have a log area?
    pass

