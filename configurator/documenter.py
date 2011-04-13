'''
Should be able of supplying documentation on (Business) Decorators and Materials
(instantiable Resources).
-Decorators: @operations
-Materials: attributes
In the future, with the use of a workflow engine, it should also work for Processes
'''
import inspect
from domain.resource.material import Material
from domain.base.decorator import Decorator


class Documenter:
    ''' Presents information on Business Decorators and Materials '''
    def __init__(self):
        self.decorators = []
        self.materials = []
        self.operations = []
        self.materials_documentations = []

    def find_classes(self, module):
        ''' finds classes in a module '''
        for name in dir(module):
           obj = getattr(module, name)
           if inspect.isclass(obj):
               #each import clause inserts imported classes in the namespace
               #thus one class can appear more than once when a module has many imports
               if (obj not in self.decorators) and (obj not in self.materials):
                  #a class is a subclass of itself, thus:
                  if issubclass(obj, Decorator):
                     if obj.__name__ != 'Decorator':
                         self.decorators.append(obj)
                  elif issubclass(obj, Material):
                     #Resources are in fact subclasses of Material
                     if obj.__name__ != 'Material':
                         self.materials.append(obj)

    def list_decorators_operations(self):
        ''' for each decorator, lists its @operations '''
        for decorator in self.decorators:
            for method_name, method_object in inspect.getmembers(decorator, inspect.ismethod):
                if hasattr(method_object,'category'):
                    self.operations.append([decorator, method_object])

    def list_materials_documentations(self):
        ''' for each material, lists its documentation '''
        for material in self.materials:
            self.materials_documentations.append([material, material.__doc__])

