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

    @classmethod
    def get_instance(cls):
        return cls()
    #/Singleton machinery

    def check_decoration_rules(self, decorator_class, decoration_candidate):
        '''Checks all decoration rules of a given decorator upon a given decoration candidate'''
        approved_rules = []
        refused_rules = []
        if not decorator_class.decoration_rules:
           raise ValueError('%s type has no decoration rules' % decorator_class.__name__)
        for rule in decorator_class.decoration_rules:
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

    #
    #Really ugly stuff:
    #the rules below should me managed by BankSystemRuleManager
    #when dynamic loading is ready they will leave this class
    #
    @rule('association')
    def should_be_instance_of_bank_account(self, associated):
        '''Associated object should be instance of Bank Account Decorator'''
        from bank_system.decorators.bank_account_decorator import BankAccountDecorator
        try: associated |should| be_instance_of(BankAccountDecorator)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_credit_analyst(self, associated):
        '''Associated object should be instance of Credit Analyst Decorator'''
        from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
        try: associated |should| be_instance_of(CreditAnalystDecorator)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_loan_request(self, associated):
        '''Associated object should be instance of Loan Request'''
        from bank_system.resources.loan_request import LoanRequest
        try: associated |should| be_instance_of(LoanRequest)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_have_employee_decorator(self, associated):
        '''Associated object should be previously decorated by Employee'''
        from bank_system.decorators.employee_decorator import EmployeeDecorator
        import domain.supportive.contract_matchers
        try: associated |should| be_decorated_by(EmployeeDecorator)
        except ShouldNotSatisfied: return False
        else: return True

