class Human:
    'inner class example'
    def __init__(self):
        self.name='amit'
        self.head=self.Head()
        'here Head() is calling Class Head '

    class Head:

        def talk(self):
            return 'talking....'

if __name__ == '__main__':
    obj1=Human()
    print(obj1.name)
    print(obj1.head.talk())
