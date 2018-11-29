class justcounter:

    "data can make private or hide(protected) by defining  __"
    __secretcount=0

    def count(self):
        self.__secretcount += 1
        print(self.__secretcount)


counter=justcounter()
counter.count()
counter.count()

print(counter._justcounter__secretcount)

"Python protects those members by internally changing the name to include the class name."


