class employee:

    raise_amount =1000
    def __init__(self,firstname,lastname,pay):
        self.firstname=firstname
        self.lastname=lastname
        self.pay=pay
        self.email=firstname+'.'+lastname+'@'+'comapany.com'

    def fullname(self):
        return self.firstname+' '+self.lastname

    def payment(self):
        return (self.pay*self.raise_amount)



class devloper(employee):
    raise_amount = 2000

    def __init__(self, firstname, lastname, pay,course):
        super().__init__(firstname,lastname,pay)
        self.course=course


class manger(employee):
    def __init__(self, firstname, lastname, pay,employees=None):
        super().__init__(firstname,lastname,pay)
        if employees is None:
            self.employees = []
        else :
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--->',emp.fullname())



'''obj=employee('amit','kumar',5000)
print(obj.fullname())
print(obj.payment())'''

obj=employee('amit','kumar',5000)

obj1=devloper('test','automation',70,'python')

obj2=devloper('rat','run',90,'java')

#print(obj1.fullname())
#print(obj1.email())
#print(obj1.course)

mgr1=manger('corey','schafer',5000,[obj2])

mgr1.add_emp(obj1)
#print(mgr1.email)
getattr(mgr1,'email')
mgr1.print_emp()