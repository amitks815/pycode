class math:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c= c



    def sum(self,a,b,c):

        return self.a+self.b+self.c
    def sum(self,a,b):
        return self.a+self.b

val=math(1,2,3)

print('add :',val.sum() )

print('sub :',val.sum())