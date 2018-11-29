class name1:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def name(self):

        return self.name

class age:

    def __init__(self, name, age):
        name1.__init__(name,age)

    def age(self):
        return self.age



c1=name1('amit',22)
print(c1.name)
c2=age()

print  (c2.name1.name)