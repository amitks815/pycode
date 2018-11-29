def largest(list1):
    large=list1[0]
    large2=list1[0]
    for i in list1:
        if i>large:
            large=i
        elif large2!=large and large2<i:
            large2=i



    return large
list1=[2,1,4,5,7,3,4,5]
print(largest(list1))