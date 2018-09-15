#!/usr/bin/python3

# import exerc3
from exerc3 import Conta, Poupanca

c1 = exerc3.Conta('daniel',123,1500)
c2 = exerc3.Conta('maria',456,2000)

c2.transferir(500, c1)

print(c1.saldo, c2.saldo, sep="\n")