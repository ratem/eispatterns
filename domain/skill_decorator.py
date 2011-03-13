from domain.decorator import Decorator
from should_dsl import should
from inspect import getsource
#from string import split
from domain.immaterial import Immaterial

class SkillDecorator(Decorator):
    def __init__(self):
        Decorator.__init__(self)
        self.description = "This is a skill decorator"
        self.skill_description = None

    def check_rules_of_association(self, decorated):
        try:
            self.rule_should_be_immaterial_instance(decorated)
        except: #need a customized exception here
            raise ValueError('Immaterial instance expected, instead %s passed' % type(decorated))

    def query_rules_of_association(self,query=None):
        rule_method = getsource(self.rule_should_be_immaterial_instance)
        #very stupid code
        #splits after the method signature
        rule_method_code = rule_method.split('\n')
        #strip the method signature
        rule_method_code = rule_method_code[1]
        #strip whitespaces
        rule_method_code = rule_method_code.lstrip(' ')
        return rule_method_code

    def decorate(self, decorated):
        pass

    def rule_should_be_immaterial_instance(self, decorated):
        decorated |should| be_instance_of(Immaterial)

