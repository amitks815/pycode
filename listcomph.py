

square=[i**2 for i in range(1,10) if i>3]

print(square)


list1=['amit','sumit','atul','abram','bhaskar']

val=[item for item in list1 if item.startswith('a')]

print(val)


list2=[('amit',1990),('sumit',1994),('atul',1989),('abram',1988),('bhaskar',1990)]

res=[name for (name,year) in list2 if year>1990 ]

print(res)


a=[1,2,3,4]
b=[5,6,7,8]

val1=[(x,y) for x in a for y in b]

print(val1)