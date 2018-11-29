

def decorator_func(org_fun):

    def wrapper():

        print('wrapper executed this befor')

        return org_fun()

    return  wrapper



@decorator_func
def display(name):

    print('it ran')

# obj=decorator_func(display('amit'))

display()


