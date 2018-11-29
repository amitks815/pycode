class democlass():
    """ This is demonstration class """

    pass
my_instance1=democlass()
print(democlass.__doc__)
print(my_instance1.__doc__)
print(dir(democlass))
print(id(my_instance1))
print(type(my_instance1))
 
# Assigning a python object

my_instance2=my_instance1

print(my_instance2.__doc__)