list1 = [25, 18, 9, 41, 26, 31]
list2 = [25, 45, 3, 32, 15, 20]

a=list1.sort()
b=list2.sort()

c=[i+j for i in a for j in b]

print(c)