class Dog2:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age): # Instance attribute
        self.name = name
        self.age = age
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Dog2:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

miles = Dog2("Miles", 4, "Jack Russell Terrier")
buddy = Dog2("Buddy", 9, "Dachshund")
jack = Dog2("Jack", 3, "Bulldog")
jim = Dog2("Jim", 5, "Bulldog")
print(miles.name, buddy.name, jack.name, jim.name)
# print(miles.description())

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles1 = JackRussellTerrier("Miles1", 4)
print(miles1)
print(miles1.speak())