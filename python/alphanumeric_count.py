# str= input("Enter the string :")
# count1=0
# count2=0
#
# for i in str:
#     if i.isdigit():
#         count1+=1
#     else:
#         count2+=1
#
# print('string contain {} numeric and {} alphabetic'.format(count1,count2))


# str= input("Enter the string :")
# word=input('enter the word')
#
# a=[]
# count=0
# a=str.split(' ')
# for i in range(0,len(a)):
#     if word==a[i]:
#         count+=1
# print('no of word count is {}'.format(count))
#
# str= input("Enter the string :")
#
# a=[]
# c=[]
# a=str.split(' ')
#
# for i in a:
#     b=i[0]
#     c.append(b)
#
# d=dict(list(zip(c,a)))
# print(d)


l1=[1,3,4,7,2,5]
l2=[2,5,6,8]
a=[x for x in l1 if x not in l2]
print(l2.extend(a))
# for i in l1:
#     if i not in l2:
#         l2.append(i)
#
# print(l2)



