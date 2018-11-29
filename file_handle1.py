file=open("write_file.txt",'r+')
file.write("\n give me some sun shine")


print(file.read(50))

print(file.tell())

file.seek(55)

print(file.read(10))



# for line in file:
#
#     token =line.split(' ')
#
#     print(len(token))
#
#     print(line)
#

# val=file.read()
#
# print(val)
file.close() 