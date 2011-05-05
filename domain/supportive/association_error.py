class AssociationError(Exception):
    ''' Specific for contracts that regulate association actions '''
    def __init__(self, any_value):
        self.value = any_value
    def __str__(self):
        #returns a string representation of any object passed
        return repr(self.value)

