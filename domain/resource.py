from domain.business_entity import BusinessEntity


class Resource(BusinessEntity):

    def __init__(self):
        BusinessEntity.__init__(self)
        self.oid  = None
        self.unit = None

