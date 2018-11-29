list1=[[1,2,3],[2,5,7],[10,11,12],[9,8,7]]
l=[]
temp=0
i=0
while i<len(list1):
    a=sum(list1[i])
    l.append(a)

    i+=1
    print(max(l))

# print(l)

for val in list1:
    if sum(val)==max(l):

        print(val)

#
#
# for i in list1:
#     a=sum(i)
#     # print (a)
#     temp=a
#     print(a, temp)
#     if temp<a:
#
#         print(temp)
#
#     # print(sum(temp)

lst=[20,13,90,14,90,10]

print([x for x in lst if x>10])