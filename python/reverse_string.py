# str=input("Enter the string :")
#
# string=''
#
# for i in str:
#     print(i)
#     string=i+string
#
# print(string)
#

s=[("amit",1),("ami",2)]
d={}

for k,v in s:
    d[k].append(v)

print(d)