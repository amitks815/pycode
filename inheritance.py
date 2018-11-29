from class5 import *

class devloper(employee):
    raise_amount = 2000

    def __init__(self, firstname, lastname, pay,course):
        super().__init__(firstname,lastname,pay)
        self.course=course

    pass


obj1=devloper('test','automation',70,'python')

print(obj1.fullname())
print(obj1.email)
print(obj1.course)


#print(help(devloper))