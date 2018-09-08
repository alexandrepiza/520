#!/usr/bin/python3
# 1. Dado a matriz, calcular a soma das diagonais
# matriz = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#exemplo = 1+5+9+3+5+7
linha1=[1,2,3]
linha2=[4,5,6]
linha3=[7,8,9]

#Solução 1
print('Solução 1',end='\n')
matriz=[linha1,linha2,linha3]
result=matriz[0][0]+matriz[1][1]+matriz[2][2]+matriz[0][2]+matriz[1][1]+matriz[2][0]
print(result)

#Solução 2
print('Solução 2',end='\n')
a = 0
b = 0
cont = 0

for x in matriz:
    a += x[cont]
    cont += 1
    b += x[-cont]

print(a+b)

#Solução 3
print('Solução 3',end='\n')
a = 0
b = 0
cont = 0

for count,x in enumerate(matriz):
    a += x[cont]
    b += x[-(cont+1)]

print(a+b)

#Solução 4
print('Solução 4',end='\n')
soma = 0

for count,x in enumerate(matriz):
    soma += x[cont]
    soma += x[-(cont+1)]

print(soma)