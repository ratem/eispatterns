class Configurable:
    def __init__(self):
        self.tag           = None
        self.label         = None
        self.configuration = None

    def define_tag(self,tag=None):
        ''' if not passed as a parameter, defines tags by some algorithm '''
        if tag == None:
            self.tag = 0 #id generation algorithm goes here
        else:
            self.tag = tag

    def configure(self, configuration):
        #each subclass has a configurator_class class attribute
        if (configuration.__class__.__name__ == self.configurator_class):
            self.configuration = configuration
        else:
            raise KeyError,'Non compatible configuration'

    def todo(self):
        ''' usually redefined and renamed by each abstract concept '''
        return self.tag

