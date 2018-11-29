from collections import *

c=Counter({'a':3,'b':2,'c':1})

print(c)

d=Counter("hello")

print(d)

e=Counter([1,2,3,4,4])

print(e)


f=Counter(a=2,b=1,c=3)
print(f)


#updating counter
e.update([12,13])
print(e)


#accessing counter

for i in e.elements():
    print(i,e[i])



#Default dict

f=defaultdict(list)

for i,j in [('a',(1,2)),('b',(3,4))]:

    f[i].append(j)


print('**',f)



#Orderdict
