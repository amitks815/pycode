class fruit:

    __size='small'

    def __init__(self,name,color):
        self.name=name
        self.color=color

    def details(self):

        self.__size

        print('name of the fruit is {} and color is {} '.format(self.name,self.__size))



obj=fruit('apple','red')

obj.details()

