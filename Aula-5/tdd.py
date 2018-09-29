#!/bin/usr/python3

from unittest import TestCase, main

def validar_par(num: int)-> bool:
    '''
    Função para validar um número par.
    Args:
        num - recebe um numero do tipo inteiro
    Retorno: Booleano
    '''
    # Aqui será implementado a logica
    try:
       return True if int(num) % 2 == 0 else False
    except Exception:
        return None

    # if num % 2 == 0:
    #     print(num,' é par')

class Testes(TestCase):
    def test_par(self):
        self.assertEqual(validar_par(4), True)
        self.assertEqual(validar_par(1000), True)
    # def test_impar(self):
        self.assertEqual(validar_par(5), False)
        self.assertEqual(validar_par(1001), False)
    # def test_string(self):
        self.assertEqual(validar_par('102'), True)
        self.assertEqual(validar_par('1059'), False)
        self.assertEqual(validar_par('string'), None)

if __name__ == "__main__":
    main()