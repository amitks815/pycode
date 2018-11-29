import os

os.chdir('C:\\Users\\kumaami3\\PycharmProjects\\')

for dirpath,dirnames,filenames in os.walk('C:\\Users\\kumaami3\\PycharmProjects\\pycode'):

    print('current path:',dirpath)
    print('directories:',dirnames)

    print('filename :',filenames)

    print()

    print(os.environ.get('HOME'))