#from domain.multiton import multiton
from domain.configurable import Configurable

class ResourceConfiguration(Configurable):

    template_configuration_text = '[A/An] <resource> is [a/an] <type>, <short description>, measured by <unit>'

    def __init__(self):
        Configurable.__init__(self)
        self.description        = None
        self.type               = None
        self.unit               = None

    def parse(self, configuration_text):
        #elesbom code goes here
        return 0

