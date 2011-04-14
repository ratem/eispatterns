'''
Should be able of supplying documentation on (Business) Decorators and Materials
(instantiable Resources).
-Decorators: @operations
-Work Items: attributes
In the future, with the use of a workflow engine, it should also work for Processes
'''
import inspect
from domain.resource.work_item import WorkItem
from domain.base.decorator import Decorator


class Documenter:
    ''' Presents information on Business Decorators and Materials '''
    def __init__(self):
        self.decorators = []
        self.work_items = []
        self.operations = []
        self.work_items_documentations = []
        self.found = []

    def find_classes(self, module):
        ''' finds classes in a module '''
        for name in dir(module):
           obj = getattr(module, name)
           if inspect.isclass(obj):
               #each import clause inserts imported classes in the namespace
               #thus one class can appear more than once when a module has many imports
               if (obj not in self.decorators) and (obj not in self.work_items):
                  #a class is a subclass of itself, thus:
                  if issubclass(obj, Decorator):
                     if obj.__name__ != 'Decorator':
                         self.decorators.append(obj)
                  elif issubclass(obj, WorkItem):
                     #Resources are in fact subclasses of WorkItem
                     if obj.__name__ != 'WorkItem':
                         self.work_items.append(obj)

    def get_decorators_operations(self):
        ''' for each decorator, lists its @operations '''
        for decorator in self.decorators:
            for method_name, method_object in inspect.getmembers(decorator, inspect.ismethod):
                if hasattr(method_object,'category'):
                    self.operations.append([decorator, method_object])

    def get_work_items_documentations(self):
        ''' for each WorkItem, lists its documentation '''
        for work_item in self.work_items:
            self.work_items_documentations.append([work_item, work_item.__doc__])

    #simple search
    def search_term(self, term):
        self.found = []
        term.lower()
        for decorator in self.decorators:
            if decorator.__doc__.lower().find(term) != -1:
                self.found.append([decorator.__name__, decorator.__doc__])
        for decorator, method_object in self.operations:
            if method_object.__doc__.lower().find(term) != -1:
                self.found.append([decorator.__name__, method_object.__doc__])
        for work_item, work_item.__doc__ in self.work_items_documentations:
            if work_item.__doc__.lower().find(term) != -1:
                self.found.append([work_item.__name__, work_item.__doc__])

