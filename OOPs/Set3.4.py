from datetime import date

class Person():
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    
    #Class method
    @classmethod
    def frombirthyear(cls, name, year, hobby):
        return cls(name, date.today().year - year, hobby)
    
    @staticmethod
    def isadult(age):
        return(age > 18)
person1 = Person("smita", 1997, "Ukulele")
print("Check")
print(person1.frombirthyear("smita", 1997, "running").age)

print(Person.isadult(22))