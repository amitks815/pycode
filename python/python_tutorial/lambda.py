a=2
b=3
val=lambda a,b:a+b

print(val)

li={1,2,3}

mylist=lambda i:list(i)

makemylist=mylist(li)

print(makemylist)

a1=list(map(lambda i:i,li))

print(a1)



x=lambda i:i+1

y=x(1)

print(f'f={y}')

w=1
z=2
y=lambda :w+z
print(y())


#filter

itm=[1,2,3,4,5,6,7,8]
a1=list(filter(lambda x:x%2==0,itm))


print(a1)
