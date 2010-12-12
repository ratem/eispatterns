class ResourceConfiguration(object):

    template = '[A/An] <resource> is [a/an] <type>, <short description>, measured by <unit>'

    def __init__(self):
        self.configuration = None
        self.version       = None

    def parse(self):
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

