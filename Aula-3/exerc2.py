#!/usr/bin/python3

class Dog():
    '''Tentando abstrair um cachoro'''
    def __init__(self, nome, idade, raca):
        self.nome=nome
        self.idade=idade
        self.raca=raca
    def latir(self):
        print('auauau')
    def dormir(self):
        print('zzzzzz')
    def falar(self, dizer:str):
        print(dizer)
    #def __str__(self):
    #    return 'nome = {}, idade = {}, raca = {}'.format(self.nome, self.idade, self.raca)

dog1 = Dog('bilu',2 ,'pitbull')
dog2 = Dog('rex',3 ,'poddle')

print(dog1.nome)
print(dog1.nome.upper())
dog2.latir()
print(dir(dog1))
dog2.falar('oi')
print(dog1.__str__)
print(dog2.__doc__)