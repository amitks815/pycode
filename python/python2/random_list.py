# import random
# list1=[7,6,2,5,4,3]
# print(random.choice(list1)
#
#
#
#
#
# def second_smallest(numbers):
#   dup_items = set()
#   uniq_items = []
#   for x in numbers:
#     if x not in dup_items:
#       uniq_items.append(x)
#       dup_items.add(x)
#   uniq_items.sort()
#   print(uniq_items)
#   return  uniq_items[1]
#
# print(second_smallest([1, 2, -8, -2, 0, -2]))
# print(second_smallest([1, 2, -2, -2]))

# a=0
# print(str(a))
# list1=[0,1,2,3,4,5]
# list1=['0','1','2']
# # x=int("".join(map(str(list1))))
# #
# # print(x)
# str1=''
# str2=''
# for i in list1:
#     print(i)
#     str1=str1+str(i)
#     str2 = str(i)+str2
# print(str1)
# print(type(int(str2)))


# li=['abc','bde','amit']
#
# for i in li:
#     if str(i).startswith('a'):
#         print('a',str(i))
#     else:
#         print('b',str(i))


li=[3,2,5,6,7,3,9]
print(max(li,key=lambda x:int(x)))

print(max(li))