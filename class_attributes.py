class employee:
    'common base class for all employee'
    empcount=0

    def __init__(self,name ,pay):
        self.name=name
        self.pay=pay
        employee.empcount += 1

    def displaycount(self):
        print("Total number of employee %d" %  employee.empcount)

    def displayemployee(self):
        print('name :',self.name ,'salary :' ,self.pay)

print("employee.__doc__    :",employee.__doc__)
print("employee.__name     :",employee.__name__)
print("employee.__module__ :",employee.__module__)
print("employee._bases__   :",employee.__bases__)
print("emloyee.__dict__    :",employee.__dict__)
print("employee(help)      :", help(employee))

