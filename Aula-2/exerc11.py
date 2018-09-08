#!/usr/bin/python3

def soma(x, y):
    print(x+y)
    
soma(y=2,x=6) # passagem de parametros nomeado
soma(1,5) # passagem de parametros posicional
soma(3,7)

def soma2(x:int=2, y:int=2)-> int:
    '''Este texto serve para dar ajuda sobre a função. Por exemplo: \
Esta função precisa de dois parametros (números inteiros) que serão somadas.'''
# Após os dois pontos "int=2" estou definidos os parametros padrão.
    return x+y

print()    
print(soma2(y=2,x=6)) # passagem de parametros nomeado
print(soma2(1,5)) # passagem de parametros posicional
print(soma2(3,7))
print(soma2())
