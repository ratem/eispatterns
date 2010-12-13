class ResourceConfiguration(object):

    template = '[A/An] <resource> is [a/an] <type>, <short description>, measured by <unit>'

    def __init__(self):
        #retrieve(mask, version) will set these values
        self.mask          = None
        self.version       = None
        self.configuration = None
        self.description   = None
        self.type          = None
        self.unit          = None


    def parse(self, mask, version):
        ''' parses configuration '''
        pass

    def persist(self):
        ''' persists configuration '''
        pass

    def retrieve(self, mask, version):
        ''' retrieves configuration '''
        pass

    def configure(self, resource):
        ''' configures resource '''
        pass

    def list_configurations(self, mask):
        ''' list configurations of a mask '''
        pass

