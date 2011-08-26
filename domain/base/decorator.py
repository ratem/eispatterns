from domain.base.business_entity import BusinessEntity
from domain.supportive.rule_manager import RuleManager


class Decorator(BusinessEntity):

    def __init__(self):
        self.description = None

    def decorate(self, decoration_candidate):
        passed, approved_rules, refused_rules = RuleManager.get_instance().check_decoration_rules(self,decoration_candidate)
        if passed:
           self.decorated = decoration_candidate
           decoration_candidate.decorate(self)
        return passed, approved_rules, refused_rules

