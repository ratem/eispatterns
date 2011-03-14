from domain.node.node import Node


class Organization(Node):

    def __init__(self):
        Node.__init__(self)
        self.nodes = []

