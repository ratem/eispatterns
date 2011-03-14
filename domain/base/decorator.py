from domain.base.business_entity import BusinessEntity


class Decorator:
    def __init__(self):
        self.oid         = None
        self.state       = None
        self.decorated   = None
        self.description = None

    def check_rules_of_association(self, decorated):
        pass

    def query_rules_of_association(self,query=None):
        pass

    def decorate(self, decorated):
        pass

