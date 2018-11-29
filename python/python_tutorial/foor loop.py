li=['a','b','c','d']

for i in range(len(li)):
    print(li[i])


for i in range(10):
    print(i)
    if(i==7):
        break
else:
    print("Reached else")

print('*****************************')

for i in range(10):
    print(i)
    if(i==7):
        continue
else:
    print("Reached else")

print('*****************************')

for i in range(1,6):
    for j in range(i):
        print('#',end=' ')
    print("\n",end='')


for i in 'help':
    pass
print(i)