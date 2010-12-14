class ResourceConfiguration:

    template = '[A/An] <resource> is [a/an] <type>, <short description>, measured by <unit>'

    def __init__(self):
        #should be implemented as a singleton of a given key composed by mask and version
        #retrieve(mask, version) will set these values
        self.configuration_text = None
        self.mask               = None
        self.version            = None
        self.description        = None
        self.type               = None
        self.unit               = None


    def parse(self, mask, version):
        ''' parses configuration '''
        pass

    def persist(self):
        ''' persists configuration '''
        pass

    def retrieve(self, mask, version):
        ''' retrieves configuration '''
        pass

    def list_configurations(self, mask):
        ''' list configurations of a mask '''
        pass

