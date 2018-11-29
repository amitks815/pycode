val=lambda x: x*2+1

print(val(2))

val1=(lambda x,y:x if x>y else y)

print(val1(2,3))

val2=lambda x,y:max(x,y)

print(val2(7,6))

val3=lambda x: x**2

print(val(3))


fullname= lambda f_N,L_N :f_N.strip().title()+' '+L_N.strip().title()

print(fullname('amit', 'kumar'))