#!/usr/bin/python3
convidados = ['daniel','maria','joao']

try:
    num=int(input('Digite posição do convidado: '))
    print(convidados[num])
except ValueError as ver:
    print('Value! Apenas números.')
    exit()
except NameError as ner:
    print('Name! Apenas números.')
    exit()
except IndexError as ier:
    print('Index! Posição na lista inexistente. Existem {} convidados.'.format(len(convidados)))
    exit()
except Exception as exceper:
    print('Erro!: '.format(exceper))
