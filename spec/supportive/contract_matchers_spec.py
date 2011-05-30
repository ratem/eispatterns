import unittest
from should_dsl import should, should_not
from domain.supportive.contract_matchers import be_decorated_by

class Node(object):
    def __init__(self):
        self.decorators = {}

class Decorator(object):
    ''' Some decorator '''
    pass

class ContractMatchersSpec(unittest.TestCase):

    def it_checks_if_a_given_node_can_be_decorated_by_a_decorator(self):
       a_node = Node()
       a_decorator = Decorator()
       a_node |should_not| be_decorated_by(a_decorator)
       a_node.decorators[Decorator.__doc__] = a_decorator.__class__
       a_node |should| be_decorated_by(a_decorator)

