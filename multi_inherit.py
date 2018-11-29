class parent:

    "this is doc srting"
    var1=1
    def func1(self):
        pass

class child(parent):
    var2=2
    def func2(self):
        pass

p=parent()

c=child()

print(p.__doc__)

print(issubclass(child,parent))

