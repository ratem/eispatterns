import unittest
from should_dsl import should
from ludibrio import Stub
from domain.maskable import Maskable

class MaskableSpec(unittest.TestCase):

    def setUp(self):
        self.maskable = Maskable()

    def it_defines_a_todo_method(self):
        #todo is just a protocol
        pass

    def it_obtains_a_configuration(self):
        #Stubs a configuration object
        with Stub() as configuration:
            configuration.mask >> 'a mask'
            configuration.version >>'a version'
        #expected_configuration_attributes is defined only in subclasses, forced below
        self.maskable.expected_configuration_attributes = ['mask','version']
        self.maskable.configure(configuration)
        self.maskable.configuration.mask |should| equal_to('a mask')
        self.maskable.configuration.version |should| equal_to('a version')
#       resource.configuration |should| be(configuration)

    def it_defines_a_tag(self):
        #first method's scenario
        self.maskable.define_tag()
        self.maskable.tag |should| equal_to(0)
        #second method's scenario
        self.maskable.define_tag(10)
        self.maskable.tag |should| equal_to(10)

