fo=open("write_file.txt",'w+')


fo.write("i am python !")
fo.seek(0)

cont=fo.read()

print(cont)

fo.close()



