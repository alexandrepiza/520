#!/bin/usr/python3

def validar_par(num: int)-> bool:
    '''
    Função para validar um número par.
    Args:
        num - recebe um número do tipo inteiro
    Retorno: Booleano
    '''
    if isinstance(num, int):
        return True if num % 2 == 0 else False
    elif isinstance(num, str):
        if num.isnumeric():
            return True if int(num) % 2 == 0 else False
    else:
        return None
        