from domain.base.business_entity import BusinessEntity


class Resource(BusinessEntity):

    def __init__(self):
        BusinessEntity.__init__(self)
        self.unit = None

