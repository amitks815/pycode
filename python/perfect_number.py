# num=int(input('enter the number:'))
#
# temp=[]
# temp1=[]
#
# for i in range(10,30):
#     for val in range(2,i):
#         if i%val==0:
#             temp.append(val)
#             print(temp)
# #
# # if sum(temp)==val:
# #     temp1.append()
# #    print('number is perfect')
#
# print(temp1)


# def perfect_numbers_in_range(a,b):
#     return [x for x in range(a,b+1) if sum([y for y in range(1,x) if x%y==0]) == x]
# #
# print(perfect_numbers_in_range(1,1000))

n1=int(input('enter the number'))
n2=int(input('enter the number'))

for n in range(n1,n2+1):
    sum = 0
    for y in range(1,n):
        if not n % y:
            # print(n,y)
            sum += y
           # print(sum)
    if sum == n:
        print(n, "is a perfect number")


