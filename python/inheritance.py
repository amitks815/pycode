class vehical:

    def general_usage(self):
        print('general use : transportation')


class car(vehical):

    def __init__(self,wheel):

        self.wheel=wheel
        self.has_roof='true'

    def specific_usage(self):

        print('used for work transport')

class bike(vehical):

    def __init__(self, wheel):

        self.wheel=wheel
        self.has_roof='False'

    def specific_usage(self):

        print('use for racing  and trip')


class cycle(bike,car):
    def __init__(self,wheel):
        bike.__init__(self,wheel)

    print('i m cycle',self.wheel)

cl=cycle(5)
cl.specific_usage()

# cl.specific_usage()



# c=car(4)
#
# c.specific_usage()
# c.general_usage()
#
# m=bike(2)
#
# m.specific_usage()
# m.general_usage()
