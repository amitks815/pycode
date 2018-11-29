import os

# print(dir(os))
#
# cwd= os.getcwd()
#
# files=os.listdir(cwd)
#
#
# # os.makedirs('C:\\Users\kumaami3\PycharmProjects\pycode\python')
# # # os.path('C:\\Users\kumaami3\PycharmProjects\pycode\python')
# for file in files:
#     path= os.path.join(cwd,file)
#    # p  rint(os.path.split(path))
#
#     print(path)

'change current working directories with os.chdir(path)'
#
# print(os.getcwd())
#
# os.chdir('C:\\Users\\kumaami3\\PycharmProjects\\pycode\\python\\python2')
#
# print(os.getcwd())



fd =os.open('class.py',os.O_RDWR)
d_fd=os.dup(fd)
os.write(fd,"testing")


