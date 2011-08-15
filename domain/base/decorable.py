from domain.base.business_entity import BusinessEntity


class Decorable(BusinessEntity):
    def __init__(self):
        BusinessEntity.__init__(self)
        self.decorators = {}
        self.decoration_history = []

