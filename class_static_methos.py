from datetime import date

class person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def f1(self):
        pass
    
    @classmethod
    def frombirthyear(cls,name,year):


         return cls(name ,date.today().year-year)

    @staticmethod

    def isadult(age):

        return age>18


person1=person('amit',28)

person.f1()
person1.frombirthyear('amit',1990)

print(person1.name)


print (person1.age)
#print (person2.age)

print(person.isadult(21))