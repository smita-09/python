class Person:
    # Kind of constructor
    def __init__(self, name):
        self.name = name
    # Function which says hi
    def say_hi(self):
        print("Hello, my name is {}".format(self.name))

me = Person("smita").say_hi()

# Another class
class CSStudent:
    stream = "CS" # since for this variable we want it to be common over all function.
    # This is also called class varible
    def __init__(self, roll):
        self.roll = roll

     # Adds an instance variable
    def setAddress(self, address):
        self.address = address
     
    # Retrieves instance variable   
    def getAddress(self):   
        return self.address  
    
a = CSStudent(101)
a.setAddress("Prayagraj, UP")
print(a.getAddress())

# Creation of an empty class
class Test2:
    pass 