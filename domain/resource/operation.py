'''
operation is a Python Decorator which is applied to Node/Person and Node/Machine
 methods to mark them as business operations. The decorated method must have a
 docstring
'''

def operation(**attributes):
    def add_attributes(method):
        #add attributes to the method
        for attr in attributes:
            setattr(method, attr, attributes[attr])
        if method.__doc__ == None:
            raise ValueError('Operation must have a docstring')
        return method
    return add_attributes

