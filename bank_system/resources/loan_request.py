from datetime import datetime
from domain.resource.material import Material


class LoanRequest(Material):
    def __init__(self, account, value, analyst):
        Material.__init__(self)
        self.unit = 'unit'
        self.account = account
        self.value = value
        self.analyst = analyst
        self.datetime = datetime.now()

