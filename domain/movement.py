from domain.configurable import Configurable

class Movement(Configurable):

    expected_configuration_attributes = ['mask','version']
    #, 'category', 'description','source_node_mask', 'source_node_mask_version','destination_node_mask', 'destination_node_mask_version','resource_mask', 'resource_mask_version']

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

    def set_source_node(self, source):
        #mask + version or category should be allowable
        compatible_source_node = False
        if len(self.configuration.allowable_source_node_categories) != 0:
            if (source.category in self.configuration.allowable_source_node_categories):
                compatible_source_node = True
        if len(self.configuration.allowable_source_node_masks_and_versions) != 0:
            if ([source.mask, source.version] in self.configuration.allowable_source_node_masks_and_versions):
                compatible_source_node = True
        if compatible_source_node:
            self.source_node = source
        else:
            raise ValueError,'Non compatible source node configuration'

    def set_destination_node(self, destination):
        #mask + version or category should be allowable
        compatible_destination_node = False
        if len(self.configuration.allowable_destination_node_categories) != 0:
            if (destination.category in self.configuration.allowable_destination_node_categories):
                compatible_destination_node = True
        if len(self.configuration.allowable_destination_node_masks_and_versions) != 0:
            if ([destination.mask, destination.version] in self.configuration.allowable_destination_node_masks_and_versions):
                compatible_destination_node = True
        if compatible_destination_node:
            self.destination_node = destination
        else:
            raise ValueError,'Non compatible destination node configuration'

    def set_resource(self, resource):
        #mask + version or category should be allowable
        compatible_resource = False
        if len(self.configuration.allowable_resource_categories) != 0:
            if (resource.category in self.configuration.allowable_resource_categories):
                compatible_resource = True
        if len(self.configuration.allowable_resource_masks_and_versions) != 0:
            if ([resource.mask, resource.version] in self.configuration.allowable_resource_masks_and_versions):
                compatible_resource = True
        if compatible_resource:
            self.resource = resource
        else:
            raise ValueError,'Non compatible resource configuration'

