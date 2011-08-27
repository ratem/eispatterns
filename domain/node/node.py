from should_dsl import should, ShouldNotSatisfied
from domain.base.decorable import Decorable
from domain.base.decorator import Decorator
from domain.resource.resource import Resource
from domain.supportive.contract_error import ContractError


class Node(Decorable):
    def __init__(self):
        Decorable.__init__(self)
        self.input_area = {}
        self.processing_area = {}
        self.output_area = {}
        self.log_area = {}
        self.tag = None
        self.location = None

    def transfer(self, key, source_area, destination_area):
        if source_area == 'input':
            resource = self.input_area.pop(key)
        elif source_area == 'processing':
            resource = self.processing_area.pop(key)
        elif source_area == 'output':
            resource = self.output_area.pop(key)
        else:
            return False
        if destination_area == 'input': #rework!
            self.input_area[key] = resource
        elif destination_area == 'processing':
            self.processing_area[key] = resource
        elif destination_area == 'output':
            self.output_area[key] = resource
        elif destination_area == 'log': #log only receives, never sends
            self.log_area[key] = resource
        else:
            return False
        return True

    @classmethod
    def move_resource(self, key, source, destination):
        try:
            source |should| be_instance_of(Node)
        except ShouldNotSatisfied:
            raise ContractError('Node instance expected for Source, instead %s passed' % type(source))

        try:
            destination |should| be_instance_of(Node)
        except ShouldNotSatisfied:
            raise ContractError('Node instance expected for Destination, instead %s passed' % type(destination))

        try:
            resource = source.output_area.pop(key)
            resource |should| be_instance_of(Resource)
        except KeyError:
            raise KeyError('Resource with key %s not found in source node output area' % key)
        except ShouldNotSatisfied:
            source.output_area[key] = resource #put it back in the source
            raise ContractError('Resource instance expected, instead %s passed' % type(resource))
        else:
            destination.input_area[key] = resource

