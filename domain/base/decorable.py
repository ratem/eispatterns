from datetime import datetime
from should_dsl import should, ShouldNotSatisfied
from domain.base.business_entity import BusinessEntity
from domain.base.decorator import Decorator


class Decorable(BusinessEntity):
    def __init__(self):
        BusinessEntity.__init__(self)
        self.decorators = {}
        self.decoration_history = []

    def decorate(self, decorator):
        ''' Inserts decorator reference and logs datetime activation '''
        try:
            decorator |should| be_instance_of(Decorator)
        except ShouldNotSatisfied:
            raise ContractError('Decorator instance expected, instead %s passed' % type(decorator))
        else:
            self.decorators[decorator.__doc__] = decorator
            #decorator reference, datetime ativation, datetime deactivation
            self.decoration_history.append([decorator, datetime.now(), None])

    def undecorate(self, decorator):
        ''' Keeps decorator reference and logs its datetime deactivation'''
        for decorator_activation in self.decoration_history:
            #since the same decotator can be activated and deactivated many times
            #gets the one still active
            if decorator_activation[0] == decorator and decorator_activation[2] == None:
               decorator_activation[2] = datetime.now()
               return True
        return False

