str=" this is amit here amit is very kind and generous he is living in bengaluru bengaluru is one of the best city in india"

data=str.split()
dict1={}.fromkeys(data,0)

for val in data :

    dict1[val] += 1
print(dict1)

