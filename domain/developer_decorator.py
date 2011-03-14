from inspect import getsource
from should_dsl import should
from domain.base.decorator import Decorator
from domain.node.person import Person


class DeveloperDecorator(Decorator):

    def __init__(self):
        Decorator.__init__(self)
        self.description = "Development skills"
        self.language = None
        self.level = None
        self.other_skills = None

    def decorate(self, decorated):
        try:
            self.rule_should_be_person_instance(decorated)
        except: #need a customized exception here
            raise ValueError('Person instance expected, instead %s passed' % type(decorated))
        self.decorated = decorated

    def query_rules_of_association(self,query=None):
        rule_method = getsource(self.rule_should_be_person_instance)
        #very stupid code downwards
        #splits after the method signature
        rule_method_code = rule_method.split('\n')
        #strip the method signature
        rule_method_code = rule_method_code[1]
        #strip whitespaces
        rule_method_code = rule_method_code.lstrip(' ')
        return rule_method_code

    def rule_should_be_person_instance(self, decorated):
        decorated |should| be_instance_of(Person)

    def set_skills(self, language, level, other_skills):
        self.language = language
        self.level = level
        self.other_skills = other_skills

    #stupid code only to show that a resource/material/source_code must be transformed
    #must be improved to check the category of material == source_code using should_dsl
    def develop(self):
        self.source_code = 'print("hello world")'

