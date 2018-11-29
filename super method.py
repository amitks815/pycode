class human():

    def __init__(self,name,age,height):

        self.name=name
        self.age=age
        self.height=height


    def display_details(self):

        print(self.name,self.age,self.height)


class male(human):

    def __init__(self,name,age,height,salary):
        #human.__init__(self,name,age,height)

        super().__init__(name, age, height) #super is used when single inheritance take place and we use to copy the attributes and method of that class'
        self.salary=salary

        super().display_details()


    def display_male_details(self):
        print(self.name, self.age, self.height,self.salary)

m=male('amit',28,174,20000)
m.display_male_details()