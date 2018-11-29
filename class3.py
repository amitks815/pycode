class democlass:
    def demomethod(self,value):
        double_value=value*2
        return double_value
    def addit(self,x,y):
        add_val=x+y
        return add_val

obj=democlass()
obj2=democlass()
result=obj.demomethod(2)
result2=obj2.addit(2,3)
print(result)
print(result2)
     