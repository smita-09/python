#Multiple Inheritance
# Base class first
class Base(object):
    
    def __init__(self):
        self.str1 = "geek1"
        print("Base1")
# Base class second
class Base2(object):

    def __init__(self):
        self.str2 = "geek2"
        print("Base2")
# derived class
class Derived(Base, Base2):

    def __init__(self):
        Base.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)

#Object Instantiation
ob = Derived()
ob.printStrs()