#!/usr/bin/python3
nomes = ['yamin','rafael','jessica']

with open('/home/developer/520/Aula-2/nomes2.txt', 'a') as arquivo:
    arquivo.writelines([x+'\n'.title() for x in nomes])
# O modo acima é list compreention.

with open('/home/developer/520/Aula-2/nomes2.txt', 'a') as arquivo:
    for nome in nomes:
        arquivo.write(nome +'\n')