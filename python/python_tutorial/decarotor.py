def decor(func):

    def wrap():

        print('***********')

        func()

        print('***************')


    return wrap
@decor
def sayhello():
    print('hello')

# newfun=decor(sayhello)
#
# newfun()
sayhello()