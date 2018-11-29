import re

nameage=''' Amit is 28 and Sumit is 24
            Rams is 44 and Rahin is 55 '''

ages=re.findall(r'\d{1,3}',nameage)
names=re.findall(r'[A-Z][a-z]*',nameage)

print(ages)
print(names)

agedict= {}

x=0

for eachname in names:
    agedict[eachname]=ages[x]

    x=x+1

print(agedict)
