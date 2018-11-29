import re
list1=[]
with open ("file.txt") as f  :
    #content=f.readlines()
    for line in f.readlines():
        list1.append(line)
    print(list1)

pattern=(r'[A-za-z0-9.]+@[A-za-z0-9]+.[A-za-z]+')

for val in list1:

    matches=re.search(pattern,val)
    if matches:
        print(matches.group(0))
