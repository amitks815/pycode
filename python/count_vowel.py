# str='hello amit is here and he is our hero'
#
# vowel='aeiou'
#
# dict1={}
# count=dict1.fromkeys(vowel,0)
#
# for char in str:
#    if char in count:
#
#        count[char] += 1
#
# print(count)

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str='heloo !! @ %^# rat hat'

nonpon=''
for char in str:

    if char not in punctuations:
        nonpon=nonpon+char

print(nonpon)


