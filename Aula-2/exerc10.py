#!/usr/bin/python3

with open('/home/developer/520/Aula-2/texto.txt', 'r') as arq:
    conteudo = arq.readlines()

print(conteudo)

aux = []
for   x in conteudo:
    if x == '\n':
        continue
    aux.append(x)

print(aux)