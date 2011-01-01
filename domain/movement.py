from domain.configurable import Configurable

class Movement(Configurable):

    expected_configuration_attributes = ['mask','version', 'type', 'description','source_node_mask', 'source_node_mask_version','destination_node_mask', 'destination_node_mask_version','resource_mask', 'resource_mask_version']

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

    #an important remark: some movements may work with many different masks for
    #source and destination, as well as all of a given category.
    #For instance, payments should work to all category=="person".
    #The code below doesn't allow this, will correct later
    def set_source_node(self, source):
        if source.mask != self.configuration.source_node_mask:
            raise ValueError, 'Wrong source node mask: %s' % source.mask
        elif source.version != self.configuration.source_node_mask_version:
            raise ValueError, 'Wrong source node mask version: %s' % source.version
        self.source_node = source

    def set_destination_node(self, destination):
        if destination.mask != self.configuration.destination_node_mask:
            raise ValueError, 'Wrong destination node mask: %s' % destination.mask
        elif destination.version != self.configuration.destination_node_mask_version:
            raise ValueError, 'Wrong destination node mask version: %s' % destination.version
        self.destination_node = destination

    def set_resource(self, resource):
        if resource.mask != self.configuration.resource_mask:
            raise ValueError, 'Wrong resource mask: %s' % resource.mask
        elif resource.version != self.configuration.resource_mask_version:
            raise ValueError, 'Wrong resource mask version: %s' % resource.version
        self.resource = resource

