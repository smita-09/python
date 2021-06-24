#In this article, Inheritance is introduced.
#One of the major advantages of Object Oriented Programming is re-use. Inheritance is one of the #mechanisms to achieve the same. In inheritance, a class (usually called superclass) is inherited #by another class (usually called subclass). The subclass adds some attributes to superclass.
#Below is a sample Python program to show how inheritance is implemented in Python

class Person():
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def isEmployee(self):
        return False

# Inheriting parent class
class Employee(Person):
    def isEmployee(self):
        return True
emp = Person("geek1")
print(emp.get_name(), emp.isEmployee())
emp = Employee("geek2")
print(emp.get_name(), emp.isEmployee())


class Base():
    pass
class Derived(Base):
    pass
print("Check")
print(issubclass(Base, Derived))
print(issubclass(Derived, Base))
a = Base()
b = Derived()
print(isinstance(a, Base))
print(isinstance(b, Derived))