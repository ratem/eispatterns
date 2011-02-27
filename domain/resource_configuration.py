'''
.Example configuration text:
An invoice, version sale, is a document, which lists information on items sold,
measured in pages.
.Will provide:
resource.mask        = invoice
resource.version     = sale
resource.category    = document
resource.description = which lists information on items sold
resource.unit        = pages
'''

#from domain.multiton import multiton
from domain.configurator import Configurator

class ResourceConfiguration(Configurator):

    template_configuration_text = '[A/An] <resource mask> version <resource mask version> is [a/an] <category or subcategory>, <description>, measured in <unit>'

    def __init__(self):
        Configurator.__init__(self)
        self.unit = None

    def parse(self, configuration_text):
        #need a parser
        return 0

