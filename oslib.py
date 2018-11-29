import os

var= dir(os)

# for val in var :
#
#     print(val)
#
# print(os.getcwd())

os.chdir('C:\\Users\\kumaami3\\PycharmProjects\\pycode\\python')

print(os.getcwd())


os.path.join('C:\\Users\\kumaami3\\PycharmProjects\\pycode','add&sub')


print(os.path.expanduser('~'))   # print current home directory of user

patname="C:\\Users\kumaami3\PycharmProjects\pycode\class.py"

os.path.split(patname)

(dirname,filename)=os.path.split(patname)

print(dirname,filename)

(shortname,extension)=os.path.splitext(filename)

print(shortname,extension)

os.chdir('C:\\Users\\kumaami3\\PycharmProjects\\pycode')
print(os.listdir('C:\\Users\\kumaami3\\PycharmProjects\\pycode'))

#os.makedirs('testpy')

os.removedirs('testpy')