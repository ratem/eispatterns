from domain.maskable import Maskable

class Node(Maskable):

    expected_configuration_attributes = ['mask','version', 'type', 'description','processing capabilities']

    def __init__(self):
        Maskable.__init__(self)
        #while it doesn't know how to process resources, it uses an alias for todo()
        self.process_resources = self.todo
        #to be set during instantiation
        self.location = None

    def define_how_to_process_resources(self, how_to_process):
        ''' make self.process a callable object '''
        self.process_resources = how_to_process

    def define_location(self):
        ''' define node's location '''
        pass

