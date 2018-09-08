#!/usr/bin/python3

#Aqui estamos trabalhando com duas variaveis uma global e outra local com o mesmo nome
var = 10
def escopo():
    var = 5
    print(var)

escopo()
print(var)

print()

#Aqui estamos trabalhando somente com uma variavel global onde posso\
# altera-la na função porque ela está declara dentro da função
var2 = 10
def escopo2():
    global var2
    var2 = 5
    print(var2)

escopo2()
print(var2)