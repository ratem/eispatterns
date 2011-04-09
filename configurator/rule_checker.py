'''
@rules must be class methods because creating an instance for each decorator is
a problem, given that the different arguments required by different decorator
constructors. The solution is to use @rules as Class Methods, with no arguments
besides decorated.
If decorators instance attributes are needed they should be used at decorate(),
making that some object can pass the @rule tests but get an extra error while
trying to decorate() it. Anyway, checking decorators instance attributes for
decoration maybe is a bad practice, given that decorators are created for
decorating an object (having setted only very basic attributes), and not the
opposite.
'''
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
        ''' finds decorator classes in a module '''
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
        ''' finds @rules in a decorator '''
        for name, method in inspect.getmembers(decorator, inspect.ismethod):
            if hasattr(method,'rule_category'):
                self.rules.append(method)

    def check_rules(self, node):
        ''' runs, for each decorator, each rule separately '''
        for cls in self.decorators:
            for rule in self.rules:
                if rule.im_self == cls: #it is safer than im_class
                    allowable = True
                    #check http://stackoverflow.com/questions/114214/class-method-differences-in-python-bound-unbound-and-static
                    try: cls.__dict__[rule.__name__].__get__(None, cls)(node)
                    except: allowable = False #should register "why"
                else: allowable = False
            if allowable:
                self.allowable_decorators.append(cls)

