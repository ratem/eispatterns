#operation is a Python Decorator which is applied to Node/Person and Node/Machine methods


def operation(**attributes):
    def add_attributes(method):
        #add attributes to the method
        for attr in attributes:
            setattr(method, attr, attributes[attr])
        #forces the method to have a docstring
        if method.__doc__ == None:
            raise KeyError
        return method
    return add_attributes

