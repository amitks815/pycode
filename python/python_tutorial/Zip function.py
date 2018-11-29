li1=[1,2,3,4,5]
li2=[6,7,8,9,10]

for i in zip(li1,li2):
    print(i)


dictzip=dict(zip(li1,li2))
print(dictzip)

listzip=list(zip(li1,li2))

print(listzip)


setzip=set(zip(li1,li2))

print(setzip)


#unzip

val1=zip(li1,li2)
a,b=zip(*val1)

print(a,b)
