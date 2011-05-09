def rule(rule_category):
    ''' Rule is a Python Decorator to typify methods as rule of association, for them to
    work with Configurator module, @classmethod must also be applyed. If the method
    doesn't have a docstring, raises exception.'''
    def add_attribute(method):
        setattr(method, 'rule_category', rule_category)
        if method.__doc__ == None:
            raise ValueError('Rule must have a docstring')
        return method
    return add_attribute

