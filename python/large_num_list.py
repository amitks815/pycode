list1=[2,3,5,4,6,7,8,12,9,43,55,12,34]
l1=[]
l2=[]

for i in list1:

    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)

print(l1,l2)
