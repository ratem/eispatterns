'''
@rules must be class methods because creating an instance for each decorator is
a problem, given that the different arguments required by different decorator
constructors. The solution is to use @rules as Class Methods, with no arguments
besides decorated.
If decorators instance attributes are needed they should be used at decorate(),
making that some object can pass the @rule tests but get an extra error while
trying to decorate() it. Anyway, checking decorators instance attributes for
decoration maybe is a bad practice, given that decorators are created for
decorating an object (having setted only very basic attributes), thus, it starts
operating - and changing its state - only after the decoration.
'''

import sys
import inspect
from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
from bank_system.decorators.bank_account_decorator import BankAccountDecorator
from domain.supportive.contract_error import ContractError
from domain.base.decorator import Decorator


class RuleChecker:
    ''' Checks for a given node which decorators can be associated to it '''
    def __init__(self):
        self.allowable_decorators = []
        self.broken_rules = []
        self.decorators = []

    def find_decorators(self, module):
        ''' finds decorator classes in a module '''
        for name in dir(module):
           obj = getattr(module, name)
           if inspect.isclass(obj):
               if issubclass(obj, Decorator):
                  #a class is a subclass of itself, thus:
                  if obj.__name__ != 'Decorator':
                     #each import clause inserts imported classes in the namespace
                     #thus one class can appear more than once when a module has many imports
                     new_decorator = True
                     for decorator in self.decorators:
                         if obj.__name__ == decorator.__name__:
                             new_decorator = False
                             break
                     if new_decorator: self.decorators.append(obj)

    def check_rules(self, node):
        ''' for each decorator, identifies and runs each rule separately '''
        for decorator in self.decorators:
            for method_name, method_object in inspect.getmembers(decorator, inspect.ismethod):
                if hasattr(method_object,'rule_category'):
                    try:#decorator.__dict__[method_name].__get__(None, decorator)(node)
                        getattr(decorator, method_name)(node)
                    except:
                        allowable = False
                        self.broken_rules.append([decorator, method_object])
                    else:
                        allowable = True
            if allowable:
                self.allowable_decorators.append(decorator)

