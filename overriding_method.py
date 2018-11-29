class area:

    def __init__(self,a,b):

        self.a=a
        self.b=b

    def sum(self):

        return self.a+self.b
        print('doner')


class area_2(area):

    def sum(self):
        print(' accepter')



a_2=area_2(2,3)

a_2.sum()

