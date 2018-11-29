try:
    f=open('class.py')
    if f.name=='class.py':
        raise Exception

    var= bad_var

except FileNotFoundError:
     print('sorry')

except Exception as e:

    print('Error')

else:
    print(f.read())
    f.close()

