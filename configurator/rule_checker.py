import sys
import inspect
from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
from bank_system.decorators.bank_account_decorator import BankAccountDecorator
from domain.supportive.contract_error import ContractError
from domain.base.decorator import Decorator

class RuleChecker:

    def __init__(self):
        self.allowable_decorators = []
        self.decorators = []
        self.rules = []

    def find_decorators(self, module):
        for name in dir(module):
           obj = getattr(module, name)
           if inspect.isclass(obj):
               if issubclass(obj, Decorator):
                  #a class is a subclass of itself, thus:
                  if obj.__name__ != 'Decorator':
                     #import clauses in modules inserts imported classes in the namespace
                     #thus one class can appear more than once when a module has many imports
                     new_decorator = True
                     for decorator in self.decorators:
                         if obj.__name__ == decorator.__name__:
                             new_decorator = False
                             break
                     if new_decorator: self.decorators.append(obj)

    def find_rules(self, decorator):
        for name, method in inspect.getmembers(decorator, inspect.ismethod):
            if hasattr(method,'rule_category'):
                self.rules.append(method)

    def check_rules(self, node):
        self.checker = Decorator()
        #import pdb;pdb.set_trace()
        for cls in self.decorators:
            #creating an instance is a problem, because of the creation arguments
            #the solution is to use Class Methods, with standard arguments
            #if we need instance attributes for checking associations, one of
            #the default arguments must be and instance of the given class
            #this also can cause problems, thus the solution is to use getsource
            checker = cls('x')
            try:
                checker.decorate(node)
            except:
                pass
            else:
                self.allowable_decorators.append(cls.__doc__)

    def stupid_check(self,node):
        #What is done below must be done dinamically, by iterating through all decorators
        credit_analyst = CreditAnalystDecorator('x')
        try:
            credit_analyst.decorate(node)
        except:
            pass
        else:
            self.allowable_decorators.append(credit_analyst.__class__.__doc__)
        bank_account = BankAccountDecorator('x')
        try:
            bank_account.decorate(node)
        except:
            pass
        else:
            self.allowable_decorators.append(credit_analyst.__class__.__doc__)

