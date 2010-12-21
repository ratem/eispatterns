'''
Multiton Pattern:
 http://en.wikipedia.org/wiki/Multiton_pattern#Python
Usage:
 @multiton
 class MyClass:
    ...
 a=MyClass("MyClass0")
 b=MyClass("MyClass0")
 c=MyClass("MyClass1")
 print a is b #True
 print a is c #False
'''
def multiton(cls):
    instances = {}
    def getinstance(name):
        if name not in instances:
            instances[name] = cls()
        return instances[name]
    return getinstance

