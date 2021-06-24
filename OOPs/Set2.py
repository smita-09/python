# In Python, we use double underscore (Or __) before the attributes name and those attributes will not be directly visible outside.

from re import M
from numpy.f2py.crackfortran import myeval


class MyClass:
    __hidden_variable = 0

    def add(self, increment):
        self.__hidden_variable += increment
        print(self.__hidden_variable)
myObj = MyClass()
myObj.add(2)
myObj.add(5)

# print (myObj.__hiddenVariable) 
# This line will create error cause we ar trying to access a variable which ain't accessible


#Private methods are accessible outside their class, just not easily accessible.
#Nothing in Python is truly private; internally, the names of private methods and attributes are mangled and unmangled on the fly to make them seem inaccessible by their given names 

class Test1:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return "From str method of Test: a is %s," \
            "b is %s" % (self.a, self.b)
    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)

t = Test1(1234, 5678)
print(t) # This calls __str__()
print([t]) # This calls __repr__()

#If no __str__ method is defined, print t (or print str(t)) uses __repr__.
