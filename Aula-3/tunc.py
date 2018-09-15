#!/usr/bin/python3

def pessoas(*args):
    print(args)

pessoas('daniel', 'alexandre', 'joao')

def pessoas2(*nomes):
    for x in nomes:
        print(x)

pessoas2('daniel', 'alexandre', 'joaquim')

def cadastro(**kwargs):
    print(kwargs)
    print(kwargs[nome].[0])

cadastro(nome=['alexandre','vanice'], sobrenome=['piza','mora'], idade=[41,43])