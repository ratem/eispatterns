from should_dsl import should
from domain.base.decorable import Decorable
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

    #receiving resources should be through movements, however, there is still
    #the cases where the resource is created inside the Node...
    def receive_resource(self, key, resource):
        try:
            resource |should| be_instance_of(Resource)
        except:
            raise ContractError('Resource instance expected, instead %s passed' % type(resource))
        self.input_area[key] = resource

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
        elif destination_area == 'log':
            self.log_area[key] = resource

        else:
            return False
        return True

