import re

count=0

allinfo=re.findall("inform","we need to find inform him with latest informatic information")
for i in allinfo:
    count +=1
    print(i,count)


str="we need to find inform him with latest informatic information"

for i in re.finditer("inform", str):
     tup=i.span()

     print(tup)
     