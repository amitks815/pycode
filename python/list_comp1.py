a=[1,2,3,0,3,0,0,4,5,0]


b=[i for i in a if i==0]+[j for j in a if j!=0]

print(b)