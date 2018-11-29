def fibonacci():
    limit=10
    count=0
    a=0
    b=1

    while True:
        yield a
        a,b=b,a+b

        if(count==limit):
            break
        count +=1


for val in fibonacci():
    print(val,end=' ')