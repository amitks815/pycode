# def fibonaaci(num):
#
#     a=0
#     b=1
#
#     for i in range(0,num-2):
#
#         a=b
#         b=a+b
#
#         print(b)
#
#
#
#
# num=int(input("enter the number for fibbonacci series:"))
#
# fibonaaci(num)


def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)


print(F(5))
