
class democlass:
    def demomethod(self):
        print('this is demonstatre methos' )
        print("the id of self is ",id(self))
my_object=democlass()
my_object2=democlass()
print("the id of first object",id(my_object))
print("the id of second object",id(my_object2))
my_object.demomethod()
my_object2.demomethod()
print(dir(my_object))
print(dir(democlass))