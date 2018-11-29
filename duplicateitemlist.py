# list1=[1,2,3,4,3,5,2,3,6,6]
# count=1
# dict={}
# for val in list1:
#     if val in dict:
#         dict[val] =count+1
#     else:
#       dict[val] = count
print(dict)



l2=[1,2,3,4,3,5,2,3,6,6]

d=dict.fromkeys(l2,0)

for i in l2:
    d[i]+=1
print(d)