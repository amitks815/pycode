texttofind='amit'
texttoreplace='sumit'


with open ('testfile.txt','r') as fobj:

    data=fobj.read()

    freq=data.count(texttofind)

filedata=data.replace(texttofind,texttoreplace)
with open ('testfile.txt','w') as file:
    file.write(filedata)