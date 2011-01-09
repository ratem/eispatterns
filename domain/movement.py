#Note: open issue: hierarchies of categories, such as
#person->employee/individual_customer
#organization->holding/branch/organization_customer/government
#by doing this one can use super-categories to include all subcategories

from domain.configurable import Configurable
#from domain.movement_configuration import MovementConfiguration

class Movement(Configurable):

    configurator_class = 'MovementConfiguration'

    def __init__(self):
        Configurable.__init__(self)
        #while it doesn't know how to process resources, it uses an alias for todo()
        self.perform = self.todo
        #to be set during instantiation
        self.source_node      = None
        self.destination_node = None
        self.resource         = None
        self.quantity         = None
        self.datetime         = None

    def define_how_to_perform(self, how_to_perform):
        ''' make self.perform a callable object '''
        self.perform = how_to_perform

    def set_resource(self, resource):
        try:
            self.configuration.check_resource_compatibility(resource)
        except ValueError:
            raise ValueError,'Non compatible resource configuration'
        else:
            self.resource = resource

    def set_source_node(self, source):
        try:
            self.configuration.check_source_node_compatibility(source)
        except ValueError:
            raise ValueError,'Non compatible source node configuration'
        else:
            self.source_node = source

    def set_destination_node(self, destination):
        try:
            self.configuration.check_destination_node_compatibility(destination)
        except ValueError:
            raise ValueError,'Non compatible destination node configuration'
        else:
            self.destination_node = destination

