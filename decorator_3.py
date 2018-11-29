import time

def time_in(func_call):



    def wrapper(*args):
        st = time.time()

        result=func_call(*args)

        et=time.time()

        print(func_call.__name__ +'time took'+ str((et-st)*1000) + 'mil sec')

        return result

    return wrapper


@time_in
def call_square(num):

    result=[]
    for i in num:

        result.append(i*i)

    return result

@time_in
def call_cube(num):

    result=[]

    for i in num:

        result.append(i*i*i)
    return result



data=range(1,1000)

square=call_square(data)
cube= call_cube(data)
