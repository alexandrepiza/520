#!/usr/bin/python3

class Conta():
    '''Documentação\
    da classe'''
    def __init__ (self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
    def sacar(self, valor:int):
        self.saldo -= valor
        return self.saldo
    def depositar(self, valor:int):
        self.saldo += valor
        return self.saldo
    def transferir(self, valor:int, conta):
        self.saldo -= valor
        conta.depositar(valor)
        return self.saldo
    def __str__(self):
        pass

tit1 = Conta('Alexandre',456, 10000)
tit2 = Conta('Vanice',123, 15000)
print(tit1.saldo)
print(tit2.saldo)
print(tit2.sacar(2000))
tit2.transferir(2000,tit1)
print(tit1.saldo)
print(tit2.saldo)
