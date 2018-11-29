num=int(input('Enter the 3 Number :'))
rev=0
while(num>0):
    dig=num%10  #return reminder
    print(dig)
    rev=rev*10+dig
    print(rev)
    num=num//10
    print(num) #return quotient
print(rev)

