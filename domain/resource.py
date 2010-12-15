from domain.maskable import Maskable

class Resource(Maskable):

    expected_configuration_attributes = ['mask','version','type', 'description','unit']

    def __init__(self):
        Maskable.__init__(self)
        #callable, to be implemented during implementation of user stories
        self.use = self.todo()

    def define_use(self):
        ''' make self.use a callable object '''
        pass

