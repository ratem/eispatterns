from should_dsl import should
from domain.supportive.contract_error import ContractError


class RuleChecker:

    def __init__(self):
        self.allowable_decorators = []

    def can_decorate(self,node):
        self.allowable_decorators = 'Credit Analyst'

