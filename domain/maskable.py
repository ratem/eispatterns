class Maskable:
    def __init__(self):
        self.tag   = None
        self.title = None

    def define_tag(self,tag=None):
        ''' if not passed as a parameter, defines tags by some algorithm '''
        if tag == None:
            self.tag = 0 #id generation algorithm goes here
        else:
            self.tag = tag

    def configure(self, configuration):
        #expected_configuration_attributes is a class attribute defined in each subclass
        for attribute in self.expected_configuration_attributes:
            if not hasattr(configuration, attribute):
                raise ValueError, 'Missing configuration attribute: %s' % attribute
        #sets a reference to the configuration object
        self.configuration = configuration

    def todo(self):
        ''' usually redefined and renamed by each abstract concept '''
        return self.tag

