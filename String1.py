str='I am a python ... wow!'

print("str.captilize() :",str.capitalize()) #make first letter captilize

print("str.center() : ",str.center(40,'*')) # width fill with chracter for string

print("str.count():",str.count('a',0,10)) #count substring from start to end loc.

suffix='wow!'

print("str.endswith() :",str.endswith(suffix,0,40)) #TRUE if the string ends with the specified suffix, otherwise FALSE

print("str.startswith() :",str.startswith('i',0,40)) #TRUE if the string start with the specified suffix, otherwise FALSE

print("str.exapended():" ,"hello" + str.expandtabs(16))

str2='python'
str3='abc'

print(str)

print("str.find() :",str.find(str2,0,40))   #find return -1 if string couldn't find


print("str.index() :",str.index(str2,0,40))  #return error

print("str.isalnun() :",str.isalnum()) #retrun if string is alphanumeric

print("str.isalpha() :",str.isalpha())

print("str.islower() :",str.islower())

str4='THIS IS IT'

print("str.isupper() :" ,str4.isupper())

print("str.isspace() :",str.isspace())

str3='123'

print("str.isdigit() :",str3.isdigit())
print("str.isnumeric() :",str3.isnumeric())

seq=('a','b','c','d')

s='-'

res=s.join(seq)

print('join() :',res)

resl=res.split('-')

print("split ():",resl)

print("len() :",len(str))

print("ljust() :",str.ljust(25,'@')) #Returns a space-padded string with the original string left-justified to a total of width columns.

print("lower() :",str.lower())

str5="    hello world    "

print("lstrip() :",str5.lstrip())

print("rstrip() :",str5.rstrip())


print("max()  :",max(str))

print("min()  :",min(str))

print("Sapcase() :",str.swapcase())

print("Title() :",str.title()) #begin with Uppercase and rest lowercase

print("Zfill() :",str.zfill(30))






