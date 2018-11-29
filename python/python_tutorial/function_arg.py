def func1(a):

    print(a)

func1(2)

def func2(a,b):
    return a+b

print(func2(3,4))

def func3(a=2,b=1):

    print(a,b)

func3()

#def func4(name='amit,age):  this is invalid
def func4(name,age=24):

    print(f"{name} and {age}")

func4('amit',12)


def func5(*num):

    for i in num:

        print(i)


func5(1,2,3,4,5,6)


def func6(**dict1):

    for i,j in dict1.items():

        print(i,j)


dict1={1:'a',2:'b',3:'c'}


func6()