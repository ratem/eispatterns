from domain.base.business_entity import BusinessEntity


class Decorator(BusinessEntity):
    def __init__(self):
        self.description = None

    def decorate(self, decorated):
        pass

