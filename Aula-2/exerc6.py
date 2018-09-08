#!/usr/bin/python3
convidados = ['daniel','maria','joao']

try:
    ling= input('Qual é a melhor linguagem \
de programação? ')
    if ling.lower().strip() != 'python':
        raise ValueError('Linguagem incorreta!')
# precisa usar um type error do python para ser associado.
except ValueError as er:
    print(er)

# Teste de dock string
print('''
Olá Mundo!

Meu nome é Alexandre
Estou ingressão no Python!
''')