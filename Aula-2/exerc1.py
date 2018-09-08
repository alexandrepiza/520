#!/usr/bin/python3
nomes = ['daniel', 'joao', 'maria']
busca = input('Digite um nome: ')

for nome in nomes:
    if busca.lower().strip() == nome:
        print('Achei')
        break
else:
    print('Não Achei')