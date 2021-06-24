# Using super to access the class

class Dog(object):
    def __init__(self, name):
        self.name = name
    
class Breed1(Dog):
    def __init__(self, name, lang):
        super().__init__(name)
        self.lang = lang 
    
    def printX(self):
        print(self.name, self.lang)

d = Breed1("Miley", "Bhaw")
d.printX() 