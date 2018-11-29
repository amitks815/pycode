def decor(func):
    def wrap():
        print("$$$$$$$$$$$$$$$$$$$$$$")
        func()
        print("$$$$$$$$$$$$$$$$$$$$$$")
    return wrap



@decor
def sayhello():
    print("Hello")

# newfunc=decor(sayhello)

sayhello()

# newfunc()