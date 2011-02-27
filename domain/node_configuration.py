'''
.One can supply lists of specific masks and/or lists of categories of resources
that can be processed by the node. Example configuration
text:
A printer, version laser, is a IT hardware, used to print documents in general,
able of processing resources of type invoice (sale), or generacally of the
category document.
.Will provide:
node.mask        = printer
node.version     = laser
node.category    = IT hardware
node.description = used to print documents in general
node.allowable_resource_masks_and_versions = [['invoice','sale']]
node.allowable_resource_categories         = ['document']
'''

#from domain.multiton import multiton
from domain.configurator import Configurator

class NodeConfiguration(Configurator):

    template_configuration_text = '[A/An] <node mask> version <node mask version> is [a/an] <category or sub category>, <description>, able of processing resources {of [type/types] <list of allowable resource masks with versions>} {,or generically} {of the [category/categories] <list of allowable resource categories>}'

    def __init__(self):
        Configurator.__init__(self)
        self.allowable_resource_masks_and_versions = []
        self.allowable_resource_categories         = []
        self.processing_capabilities = None

    def parse(self, configuration_text):
        #need a parser
        return 0

