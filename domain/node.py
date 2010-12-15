from domain.maskable import Maskable

class Node(Maskable):

    expected_configuration_attributes = ['mask','version', 'type', 'description','processing capabilities']

    def __init__(self):
        Maskable.__init__(self)
        #callable, to be implemented during implementation of user stories
        self.process = self.todo()
        #to be set during instantiation
        self.location = None

    def define_process(self):
        ''' make self.process a callable object '''
        pass

    def define_location(self):
        ''' define node's location '''
        pass

