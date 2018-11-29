import time

import logging

logging.basicConfig(filename='info.Log',level=logging.DEBUG)

logger=logging.getLogger()

def time_in(func_call):



    def wrapper(num):
        st = time.time()

        result=func_call(num)

        et=time.time()

        tt=st-et

        print(func_call.__name__ +'time took'+ str((et-st)*1000) + 'mil sec')

        logger.info("time required for {function}={time} mil sec".format(function=func_call.__name__,time=tt))

        return result

    return wrapper


@time_in
def call_square(num):

    result=(num*num)
    return result

@time_in
def call_cube(num):
    result=(num*num*num)
    return result



square=call_square(5)
cube= call_cube(10)
