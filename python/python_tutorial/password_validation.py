'''A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12'''


passw=input("enter the password ")

item=[x for x in passw.split(',')]
print(len(item[0]))
for i in item[0] :
    if len(i)>6 and  len(i)<12:
        continue
    if re.searc

print(item)





