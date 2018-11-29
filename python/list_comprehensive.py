

list=[1,2,3,4,5]
list2=[3,4,5,6,7,8]
val=[x*y for x in list  for y in list2 ]
print(val)
print(max(list))
print(max(list,key=lambda x:int(x)))