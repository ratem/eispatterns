'''
@rules are defined as methods of the singleton RuleManager. Pay attention to
configuring the appropriate RuleManager subclass when using rules not related to
the core classes.
'''
import sys
import inspect
from domain.base.decorator import Decorator
from domain.supportive.rule_manager import RuleManager
from domain.supportive.contract_error import ContractError


class RuleChecker:
    ''' Checks for a given node which decorators can be associated to it '''
    def __init__(self):
        self.allowable_decorators = []
        self.non_allowable_decorators = []
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
            passed, approved_rules, refused_rules = RuleManager.get_instance().check_decoration_rules(decorator, node)
            if passed:
                self.allowable_decorators.append(decorator)
            else:
                self.non_allowable_decorators.append(decorator)
                self.broken_rules.append(refused_rules)

