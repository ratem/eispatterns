from should_dsl import should, ShouldNotSatisfied
from domain.supportive.rule import rule
from domain.supportive.association_error import AssociationError


def loadable_rule(rule_category, docstring, module, element):
    def build_rule(method):
        setattr(method, 'rule_category', rule_category)
        setattr(method, '__doc__', docstring)
        if method.__doc__ == None:
            raise ValueError('Rule must have a docstring')
        #Check http://code.activestate.com/recipes/52241/
        m = __import__(module.element)
        return method
    return build_rule

class RuleManager(object):
    classes_and_rules = {'SomeDecorator': ['should_be_instance_of_person']}

    #Singleton machinery
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RuleManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def check_rules_for_class(self, ruled_class, associated_candidate):
        approved_rules = []
        refused_rules = []
        type_name = ruled_class.__name__
        try:
            RuleManager.classes_and_rules |should| contain(type_name)
        except ShouldNotSatisfied:
            raise KeyError('%s type has no registered rules' % type_name)
        for rule in RuleManager.classes_and_rules[type_name]:
            approved = getattr(self.__class__, rule)(associated_candidate)
            if approved: #maybe it is the case of returning only the __doc__ ...
                approved_rules.append(getattr(self, rule))
            else:
                refused_rules.append(getattr(self, rule))
        if not refused_rules:
            return True, approved_rules, refused_rules
        else:
            return False, approved_rules, refused_rules

    #(1)rules in fact should be loaded from a configuration file
    #(2)need to develop a rule builder - through decorator
    @classmethod
    @rule('association')
    def should_be_instance_of_person(self, associated):
        '''Associated object should be instance of Person'''
        from domain.node.person import Person
        try: associated |should| be_instance_of(Person)
        except ShouldNotSatisfied: return False
        else: return True

    @classmethod
    @rule('association')
    def should_be_instance_of_machine(self, associated):
        '''Associated object should be instance of Machine'''
        from domain.node.machine import Machine
        try: associated |should| be_instance_of(Machine)
        except ShouldNotSatisfied: return False
        else: return True

