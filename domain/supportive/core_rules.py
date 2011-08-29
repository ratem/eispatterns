from should_dsl import should, ShouldNotSatisfied
from domain.supportive.rule import rule


class CoreRules(object):
    version = '0.0.1'

    #(1)rules in fact should be loaded from a configuration file and
    #(2)need to develop a rule builder
    @rule('association')
    def should_be_instance_of_person(self, associated):
        '''Associated object should be instance of Person'''
        from domain.node.person import Person
        try: associated |should| be_instance_of(Person)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_machine(self, associated):
        '''Associated object should be instance of Machine'''
        from domain.node.machine import Machine
        try: associated |should| be_instance_of(Machine)
        except ShouldNotSatisfied: return False
        else: return True

