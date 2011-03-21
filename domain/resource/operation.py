#operation is a Python Decorator which is applied to Node/Person and Node/Machine methods


def operation(**attributes):
    def add_attributes(method):
        for attr in attributes:
            setattr(method, attr, attributes[attr])
        return method
    return add_attributes

