from domain.resource_configuration import ResourceConfiguration

class Resource(object):
    def __init__(self):
        #calable, to be implemented for instantiation
        self.use = None
        #object identifier
        self.tag = None

    def configure(self, mask, version):
        configuration    = ResourceConfiguration()
        configuration.retrieve(mask,version)
        self.mask        = configuration.mask
        self.version     = configuration.version
        self.description = configuration.description
        self.type        = configuration.type
        self.unit        = configuration.unit

    def define_use(self):
        ''' make self.use a callable object '''
        pass

    def define_tag(self):
        ''' define a tag for a given object '''
        pass

