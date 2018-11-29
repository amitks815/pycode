l1=[1,2,3,6,4,5]
l2=[9,3,7,8,4,10]

l3=[]

for  i in l1:
    if i not in l2:

        l2.append(i)

print(l2)

