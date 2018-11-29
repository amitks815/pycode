# def counter():
#     i=1
#     while(i<=10):
#         yield i
#         i+=1
#
#
# for i in counter():
#     print(i)


# def my_gen(x):
#
#     while(x>0):
#
#         if x%2==0:
#
#             yield 'even'
#         else:
#
#             yield 'odd'
#
#         x-=1
#
# for i in my_gen(7):
#     print(i)
#
#
# def square(x):
#
#     for i in range(x):
#         if i*i>0:
#             yield i*i
#
# print(list(square(10)))


li=[1,2,3,4,5]
x=(i*i for i in li)
next(x)

print(x)



