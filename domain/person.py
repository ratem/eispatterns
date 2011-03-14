from domain.node import Node


class Person(Node):
    def __init__(self):
        Node.__init__(self)
        self.name = None
        self.contact_information = None

