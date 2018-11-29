class rectangle:

    def __init__(self,lenght,width):

        self.lenght=lenght
        self.width=width

    def area(self):

        area=self.lenght*self.width

        print('area of rectangle:',area)

rec=rectangle(4,4)

rec.area()
