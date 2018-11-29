try:

    a, b = 1, 0
    c = a / b


    with open('file11.txt','r') as fob:

        val=fob.readline()

        print(val)

except (ZeroDivisionError,FileNotFoundError):
    print("can not divide by 0")

