from domain.node.node import Node


class Machine(Node):
    def __init__(self):
        Node.__init__(self)
        self.manufacturer = None

