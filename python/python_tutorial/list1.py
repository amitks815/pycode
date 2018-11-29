val1=['amit','kumar',9.5]
val2=[4,32,0]

val3=[val1,val2]
print(val3)
val1.append(3)
print(val1)

val2.insert(2,5)
print(val2)

val2.reverse()

print(val2)

#sorting is not possible with int and str
val2.sort()

print(val2)

print(len(val1))
num=[9,8,44]
val2.extend(num)

print(val2)


print(min(num))
print(max(num))
print("++++++++++++++++++++++++++++++++++++++")
li=[[1,2,3],[4,5],[7,8],9]

print(li[0])


li1=[1,2,3,4,5,6]

li1[1]=[9,8]

print(li1)

a=li1[:] #or li[::]
print(a)
b=li1[::-1]
print(b)

c=li1[-2]

print(c)

print(c)

d=li1[-4:-1]
print(f"d={d}")

e=li1[:-2]
print(f"e={e}")

f=li1[-2:]
print(f"f={f}")

g=li1[1:-2]

print(f"g={g}")

del li1[1:3]
print(li1)

li1.append(3)
print(li1)

li1.reverse()

print(li1)

li1.sort(reverse=True)
print(li1)
li1.sort(reverse=False)
print(li1)

print(any(['',2,'']))

print(all(['',2,'']))

print(all(['a',2,'3']))

a=[1,2,3]




