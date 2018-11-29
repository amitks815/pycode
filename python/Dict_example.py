#sort dict data in accending and decending order

# d={0:0,1:2,2:1,5:2,7:3,3:2,4:2}
#
# val=d.items()
# l=[]
# print(val)
#
# for i in val:
#     l.append(i)
#
# l.sort()
# print('accending order :',l)
#
# l.sort(reverse=True)
#
# print('decending order :',l)

#### update the dictionary ####

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dict4={}
#
# for i in dic1,dic2,dic3:
#     dict4.update(i)
#
# print(dict4)

##### check given key is exist or not
#
# dict={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
#
# def is_keypresent(key):
#         if key in dict:
#              print('key present')
#         else:
#             print("doesn't present")
#
# is_keypresent(9)
#
#
# for key,value in dict.items():
#     print(key,value)
#
#
# print(dict.keys())
# print(dict.values())



# def print_dict(num):
#     dict1 = {}
#     for i in range(1,num+1):
#         dict1[i]=i*i
#     print(dict1)
# num = int(input("Enter the number :"))
# print_dict(num)



### multiply the value in a dict
# dict={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# res=1
# for value in dict.values():
#     res=res*value
# print(res)

# dict={1: 10, 2: 20, 4: 40, 3: 30, 5: 50, 6: 60}
#
# for key in  sorted(dict):
#
#     print(key,dict[key])

# d1={1:'a',2:'b'}
# d2={3:'c',4:'d'}
#
# d3={**d1,**d2}
# print(d3)

str='amit kumar'
k=' '.join(str)
print(k)
l=k.split()
d={}
count=0
di=d.fromkeys(l,0)

for i in l:
    di[i]+=1
    print(di[i])

print(di)