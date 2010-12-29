from domain.maskable import Maskable

class Resource(Maskable):

    expected_configuration_attributes = ['mask','version','type', 'description','unit']

    def __init__(self):
        Maskable.__init__(self)
        #while it doesn't know how to be used, it uses an alias for todo()
        self.use = self.todo

    def define_how_to_be_used(self, how_to_use):
        ''' make self.use a callable object '''
        self.use = how_to_use

