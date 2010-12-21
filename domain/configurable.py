'''
-template_configuration_text is a class attribute defined in each subclass
-parse: if the parameter is compliant to template_configuration_text, sets
    self.configuration_text to the parameter
-configure_storage: configures a storage (database, file etc)
-write: persists a configuration into the storage
-read: retrives a configuration from the storage
-versions: lists the versions of a mask
'''
class Configurable:
    def __init__(self):
        self.storage            = None
        self.configuration_text = None
        self.mask               = None
        self.version            = None

    def parse(self, configuration_text):
        ''' parses configuration '''
        pass

    def configure_storage(self, storage):
        ''' configures a storage '''
        pass

    def write(self, mask, version):
        ''' persists configuration '''
        pass

    def read(self, mask, version):
        ''' retrieves configuration '''
        pass

    def versions(self, mask):
        ''' lists versions '''
        pass

