#!/usr/bin/python3

a = lambda z: z+1
a(2)


lista=[]

for x in range(10):    
    lista.append((lambda y: y ** 2)(x+1))

print(lista)

# outra forma usando o map

print(list(map(lambda y: y ** 2, range(1,11))))
