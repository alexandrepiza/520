#!/bin/usr/python3

import Modulos.banco as banco
# está apelidando banco para o modulos.banco
import threading

if __name__ == '__main__':
    user = input('Nickname: ')
    try:
        f = threading.Thread(target=banco.select)
        f.start()
    except Exception as e:
        print('Falha ao criar thread: {}'.format(e))

    # Enquanto thred rodar em seguindo plano
    while f.isAlive:
        mens = input()
        banco.cadastrar(user, mens)