import unittest
from should_dsl import should
from domain.resource.resource import Resource
from domain.node.person import Person
from domain.node.machine import Machine
from domain.movement.transportation import Transportation
from domain.resource.operation import operation


class TransportationSpec(unittest.TestCase):

    def setUp(self):
        self.a_resource = Resource()
        self.a_person = Person()
        self.a_machine = Machine()
        self.a_transportation = Transportation(self.a_person, self.a_machine)

    def it_transports(self):
        #should throw KeyError
        (self.a_transportation.transport,'resource key') |should| throw(KeyError)
        #should work
        self.a_person.output_area['resource key'] = self.a_resource
        self.a_transportation.transport('resource key')
        self.a_machine.input_area |should| contain('resource key')

