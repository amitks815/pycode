n=[4,3,2,1]

print(list(map(lambda x :x**2,n)))

print(list(map(lambda x :x**3,n)))



temps=[("berlin",29),('delhi',40),('newyork',35)]

cel_to_fer=lambda data:(data[0],9/5*data[1]+32)

print(list(map(cel_to_fer,temps)))

