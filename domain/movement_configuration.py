'''
.One can supply lists of specific masks and/or lists of categories for each
movement element (resource, source and destination nodes). Example:
.The configuration text:
A payment, version generic, is a financial operation, used to pay services or materials, as well as employees, which moves resources of the money (generic) or stocks (preferential) kinds, or generically of the category financial resources, from organization, people categories, to organization, people categories.
.Will provide:
movement.mask        = payment
movement.version     = generic
movement.category    = financial operation
movement.description = used to pay services or materials, as well as employees
movement.allowable_resource_masks_and_versions         = {[money, generic],[stocks,preferential]}
movement.allowable_resource_categories                 = ['financial resources']
movement.allowable_source_node_masks_and_versions      = None
movement.allowable_source_node_categories              = [organization, people]
movement.allowable_destination_node_masks_and_versions = None
movement.allowable_destination_node_categories         = [organization, people]
'''

#from domain.multiton import multiton
from domain.configurator import Configurator

class MovementConfiguration(Configurator):

    template_configuration_text = '[A/An] <movement mask>, version <movement mask version>, is [a/an] <category>, <description>, which moves resources of the {<list of allowable resource masks with versions> [kind/kinds]{,or generically} {of the [category/categories] <list of allowable resource categories> [categories/category]}, from {<list of allowable source node masks with versions> kind}{, or generically from} {<list of allowable source node categories> [category/categories], to {<list of allowable destination node masks with versions> kind}{,or generically to} {<list of allowable destination node categories> [category/categories]}.'

    def __init__(self):
        Configurator.__init__(self)
        self.allowable_resource_masks_and_versions         = {}
        self.allowable_resource_categories                 = []
        self.allowable_source_node_masks_and_versions      = {}
        self.allowable_source_node_categories              = []
        self.allowable_destination_node_masks_and_versions = {}
        self.allowable_destination_node_categories         = []

    def parse(self, configuration_text):
        #elesbom code goes here
        return 0

