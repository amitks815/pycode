def countX(lst,x):
    count=0
    for ele in lst:

        if (ele==x):
            count+=1

    return count

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(countX(lst,x))


# def countX(lst, x):
#     count = 0
#     for ele in lst:
#         print(ele)
#         if (ele == x):
#             count = count + 1
#     return count
#
#
# # Driver Code
# lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# x = 8
# print(countX(lst, x))