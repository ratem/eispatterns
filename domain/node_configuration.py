#from domain.multiton import multiton
from domain.configurable import Configurable

class NodeConfiguration(Configurable):

    template_configuration_text = '[A/An] <node mask> version <node mask version> is [a/an] <type>, <description>, able of <processing capabilities>'

    def __init__(self):
        Configurable.__init__(self)
        self.processing_capabilities = None

    def parse(self, configuration_text):
        #elesbom code goes here
        return 0

