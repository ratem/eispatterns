# -*- coding: utf-8 -*-
from lettuce import step, world
from should_dsl import should

@step(u'Given I am a registered Credit Analyst with number <analyst number>')
def given_i_am_a_registered_credit_analyst_with_number_analyst_number(step):
    assert False, 'This step must be implemented'
@step(u'And an individual customer asks for a personal loan')
def and_an_individual_customer_asks_for_a_personal_loan(step):
    assert False, 'This step must be implemented'
@step(u'And the customer's account number is <account number>')
def and_the_customer_s_account_number_is_account_number(step):
    assert False, 'This step must be implemented'
@step(u'And the customer's asks for a personal loan of <desired value>')
def and_the_customer_s_asks_for_a_personal_loan_of_desired_value(step):
    assert False, 'This step must be implemented'
@step(u'When I confirm the loan request')
def when_i_confirm_the_loan_request(step):
    assert False, 'This step must be implemented'
@step(u'Then a new loan request with the <account number>, <desired value>, and <analyst number> is created')
def then_a_new_loan_request_with_the_account_number_desired_value_and_analyst_number_is_created(step):
    assert False, 'This step must be implemented'

