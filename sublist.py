list1=[1,2,3]
l=[]
for n in range(len(list1)+1):
    # print(n)
    #
    # print('************')

    for m in range(n+1,len(list1)+1):
        # print(m)
        # print('&&&&&&&&&&&&&&&&')
        # print(n,m)
        sublist=list1[n:m]

        l.append(sublist)

print(l)

l=[12,32,13]
m=[12,33,11]

print(list(set(l)-set(m)))

