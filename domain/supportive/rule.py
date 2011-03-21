#rule is a Python Decorator to typify methods as rule of association


def rule(rule_category):
    def add_attribute(method):
        setattr(method, 'rule_category', rule_category)
        return method
    return add_attribute

