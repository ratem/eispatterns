#from domain.multiton import multiton
from domain.configurator import Configurator

class ResourceConfiguration(Configurator):

    template_configuration_text = '[A/An] <resource mask> version <resource mask version> is [a/an] <category>, <description>, measured by <unit>'

    def __init__(self):
        Configurator.__init__(self)
        self.unit = None

    def parse(self, configuration_text):
        #elesbom code goes here
        return 0

