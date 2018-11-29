import re
str="hat rat sat pat"

regex=re.compile("[r]at")

str=regex.sub("food",str)

print(str)


str2=''' 
this is pythin 
which deals with program
and makes thing easy
'''

print(str2)

regex=re.compile("\n")

str2=regex.sub(" ",str2)

print(str2)
