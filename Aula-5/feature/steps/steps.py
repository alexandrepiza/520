#!/bin/usr/python3

from behave import step

def soma(x:int, y:int) -> int:
    return x + y

@step('somar "{numl}" com "{num2}"')
def test_soma(context, numl, num2):
    context.r_soma = soma(int(numl), int(num2))

@step('o resultado deve ser "{esperado}"')
def test_soma_result(context, esperado):
    assert context.r_soma == int(esperado), "descrição do erro"