# How to access parent members in a subclass?

# Dog class
class Dog(object):
    def __init__(self, name):
        self.name = name

#Dog'e breed class
class GermanShephard(Dog):
    def __init__(self, name, speak):
        Dog.name = name
        self.speak = speak
    
    def DogSprache(self):
        print(Dog.name, self.speak)

#Driver Code
dog = GermanShephard("David", "Bhaw")
dog.DogSprache()