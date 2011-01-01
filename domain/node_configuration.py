#from domain.multiton import multiton
from domain.configurator import Configurator

class NodeConfiguration(Configurator):

    template_configuration_text = '[A/An] <node mask> version <node mask version> is [a/an] <category>, <description>, able of <processing capabilities>'

    def __init__(self):
        Configurator.__init__(self)
        self.processing_capabilities = None

    def parse(self, configuration_text):
        #elesbom code goes here
        return 0

