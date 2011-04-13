'''
Should be able of supplying documentation on (Business) Decorators and Resources.
-Decorators: @operations
-Resources: attributes
Obs.: Given that 'real' resources are derived from Resource/Material, it checks
    Material subclasses.
In the future, with the use of a workflow engine, it should also work for Processes
'''
import inspect
from domain.resource.material import Material
from domain.base.decorator import Decorator


class Documenter:
    ''' Presents information on Business Decorators and Resources '''
    def __init__(self):
        self.decorators = []
        self.resources = []

    def find_classes(self, module):
        ''' finds classes in a module '''
        for name in dir(module):
           obj = getattr(module, name)
           if inspect.isclass(obj):
               #each import clause inserts imported classes in the namespace
               #thus one class can appear more than once when a module has many imports
               if (obj not in self.decorators) and (obj not in self.resources):
                  #a class is a subclass of itself, thus:
                  if issubclass(obj, Decorator):
                     if obj.__name__ != 'Decorator':
                         self.decorators.append(obj)
                  elif issubclass(obj, Material):
                     #Resources are in fact subclasses of Material
                     if obj.__name__ != 'Material':
                         self.resources.append(obj)

