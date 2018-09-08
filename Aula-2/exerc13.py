#!/usr/bin/python3

def numerar(nomearquivo,nomearquivo2):
    with open(nomearquivo,'r') as arquivo:
        lista = arquivo.readlines()
        lista2 = lista[:]

    y=0
    for x in lista:
        lista[y] = '{}- {}'.format(y+1,lista[y])
        y+=1

    with open(nomearquivo2,'w') as arquivo:
        arquivo.writelines(lista)

numerar('/home/developer/520/Aula-2/nomes.txt','/home/developer/520/Aula-2/nomes3.txt')