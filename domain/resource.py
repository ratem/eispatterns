class Resource(object):
    def __init__(self):
        #configured
        self.mask        = None
        self.description = None
        self.type        = None
        self.unit        = None
        #calable, to be implemented for instantiation
        self.use         = None

    def define_use(self):
        ''' make self.use a callable object '''
        pass

