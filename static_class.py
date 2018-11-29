class test:

    @classmethod
    def f1(cls,age):
        if age !=None:
            print(age)
    #print(help(f1))


    @staticmethod
    def f2(name):
        if name !=None:


            print(name)


    # print(help(f2))

obj=test()

# test.f1(25)
# obj.f1(26)
test.f2('amit')
obj.f2('sumit')