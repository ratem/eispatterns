class Resource:

    def __init__(self):
        #calable, to be implemented during stories implementation
        self.use = None
        #object identifier, to be implemented before instantiation
        self.tag = None

    def configure(self, configuration):
        #configuration object must comply to resource_configuration
        expected_attributes = ['mask','version','type', 'description','unit']
        for attribute in expected_attributes:
            if not hasattr(configuration, attribute):
                raise ValueError, 'Missing configuration attribute: %s' % attribute
        #sets a pointer to the configuration object
        self.configuration = configuration

    def define_use(self):
        ''' make self.use a callable object '''
        pass

    def define_tag(self):
        ''' define a tag for a given object '''
        pass

