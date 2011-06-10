from fluidity.machine import StateMachine, state, transition, InvalidTransition


class LoanProcess(StateMachine):
    ''' Loan Process Template as State Machine '''
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

