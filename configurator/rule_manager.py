import inspect
from should_dsl import should, ShouldNotSatisfied
from domain.supportive.rule import rule


#rough draft for a rule builder
def built_rule(rule_category, docstring, module, element):
    def build_rule(method):
        if docstring == None:
            raise ValueError('Rule must have a docstring')
        setattr(method, 'rule_category', rule_category)
        setattr(method, '__doc__', docstring)
        #Check http://code.activestate.com/recipes/52241/
        m = __import__(module.element)
        return method
    return build_rule

class RuleManager(object):
    #Singleton machinery
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RuleManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def check_decoration_rules(self, decoration_candidate):
        '''Checks all decoration rules of a given decorator upon a given decoration candidate'''
        #gets the decorator object, without the need of passing it as an argument
        #works only if there is a rule_manager object inside the decorator
        decorator = inspect.stack()[1][0].f_locals['self']
        #print inspect.stack()[1][0].f_locals
        approved_rules = []
        refused_rules = []
        if not decorator.__class__.decoration_rules:
           raise ValueError('%s type has no decoration rules' % decorator.__class__.__name__)
        for rule in decorator.__class__.decoration_rules:
            try:
                approved = getattr(self, rule)(decoration_candidate)
            except AttributeError:
                raise AttributeError('Rule Manager has no %s rule' % rule)
            rule_object_docstring = getattr(self.__class__, rule).__doc__
            if approved:
                approved_rules.append(rule_object_docstring)
            else:
                refused_rules.append(rule_object_docstring)
        if not refused_rules:
            return True, approved_rules, None
        else:
            return False, approved_rules, refused_rules

    def check_rule(self, rule, association_candidate):
        '''Check a single rule for a given association candidate'''
        try:
            approved = getattr(self, rule)(association_candidate)
        except AttributeError:
            raise AttributeError('Rule Manager has no %s rule' % rule)
        return approved

    #(1)rules in fact should be loaded from a configuration file
    #(2)need to develop a rule builder - through decorator
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

