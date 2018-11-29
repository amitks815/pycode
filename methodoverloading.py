class human:

    def sayhello(self,name=None):
        self.name=name
        if name is not None:
            print(self.name+' '+'hello')
        else :
            print('hello')

child=human()
child.sayhello()
child.sayhello('amit')