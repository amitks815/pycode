captials={'uk':'london','france':'paris','germany':'berlin'}

more_captials={'india':'new delhi','usa':'washington'}

captials['belgium']='brussels'

print(captials,'.....>',len(captials))

del captials['uk']

print(captials,'.....>',len(captials))

items=captials.items()
'items return a (key,value) in tuple which will be sequenced in list '
print(items)

for item in items:
    print(item)


captials.pop('france')

print(captials.keys())

print(captials.values())

if captials.get('germany')=='berlin':
    'get method retrun value of key if key doesnt present then return NONE instead of error'
    print(True)


print(captials,'.....>',len(captials))

captials.popitem()

print(captials,'.....>',len(captials))

captials.update(more_captials)

'update the dict from another dict'

print(captials)

captials.clear()

print(captials,'.....>',len(captials))


