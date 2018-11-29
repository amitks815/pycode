import random

class die:
    def __init__(self):
        self.side= 0

    def throw(self):
        self.side=random.randint(1,6)
    def get_value(self):
        return self.side

mydie=die()
for i in range(1,10):
    mydie.throw()

    print("the value thrown is :",mydie.get_value())
