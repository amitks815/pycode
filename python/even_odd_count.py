num1=int(input('Enter the starting range :'))
num2=int(input('Enter the ending range :'))

count1=0
count2=0
for i in range(num1,num2):

    if i%2==0:
        count1+=1

    else:
        count2 += 1
print('number of odd number count is {}'.format(count2))
print('number of even number count is {}'.format(count1))