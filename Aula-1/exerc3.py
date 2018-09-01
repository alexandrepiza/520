#!/usr/bin/python3

numeros = [1,5,2,6,8,9,1002,3041,762]
par=[]
impares=[]
for i in numeros:
    if i%2==0:
        par.append(i)

print('numeros pares: ',par)

#ou

par2=[z for z in numeros if z % 2 ==0] #A primeira variavel z ela é acumulativa
print('numeros pares2: ',par2)


for x in numeros:
    if x%2!=0:
        impares.append(x)

print('numeros impares: ',impares)