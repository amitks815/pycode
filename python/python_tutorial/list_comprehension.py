i=[3,4,5,6,7,8]
j=[9,11,12,13,14,18]

a=[x for x in i if x>3 if x<8]
b=[x+y for x in i for y in j if x%3==0 if x%6==0 ]
print(a)
print(b)

c=["Even" if i%2==0 else "Odd" for i in range(8)]
print(c)