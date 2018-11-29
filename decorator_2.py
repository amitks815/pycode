def mydecorator(some_func):

    def wrapper():

        print("Something is happening before some_function() is called.")

        some_func()

        print("Something is happening after some_function() is called.")


    return wrapper

@mydecorator
def just_some_func():

    print("wooohooo!")

#just_some_func =mydecorator(just_some_func)

just_some_func()

#
# @mydecorator
# def just_other_func():
#
#     print('yeaaah')
#
# just_other_func()