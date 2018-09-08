#!/usr/bin/python3

with open('/home/developer/520/Aula-2/nomes.txt','r') as arquivo:
    lista = arquivo.readlines()
    lista2 = lista[:]

y=0
for x in lista:
    lista[y] = '{}- {}'.format(y+1,lista[y])
    y+=1

with open('/home/developer/520/Aula-2/nomes3.txt','w') as arquivo:
    arquivo.writelines(lista)

#print(lista)

#outra forma somente escrita
with open('/home/developer/520/Aula-2/nomes4.txt','w') as arquivo:
    for cont ,x in enumerate(lista2):
        arquivo.writelines('{}- {}'.format(cont +1,x))