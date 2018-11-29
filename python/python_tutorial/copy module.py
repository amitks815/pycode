a=[1,2,3,4]
b=a

print(a,b)

a[2]=5

print(a,b)

import copy
#shallow copy
a1=[1,2,[3,4],5]
c=copy.copy(a1)

print(c)

c[2][1]=6

print(a1)
print(id(a1))
print(c)
print(id(c))

print("******************************")
#deep copy

a2=[1,2,3,4,5]
c1=copy.deepcopy(a2)

print(c1)

c1[2]=6

print(a2)
print(id(a2))
print(c1)
print(id(c1))
