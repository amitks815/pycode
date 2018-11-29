print(dir(tuple))

tup=('a','b','c')
tup2=('d','e')

print(tup.count('a'))
print(tup.index('a'))

#tup.__add__(tup2)
#abc=tup.__sizeof__()
le=tup.__len__()
print(le)
#print(abc)
'list to tuple and tuple to list conversion'
list1=list(tup)
tup1=tuple(list1)
print(tup1)
print(list1)


seq={'as':'bs','a':'b'}

print(type(seq))

atuple=tuple(seq)

print(atuple)

