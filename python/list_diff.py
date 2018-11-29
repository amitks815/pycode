l1=[10,20,25,30,45]
l2=[10,45]

a=[i for i in l1+l2 if i not in l1 or i not in l2]
print(a)