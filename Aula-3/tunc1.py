#!/usr/bin/python3

def ler_arquivo(arquivo):
    '''função para ler arqivo'''
    with open(arquivo, 'r')as arq:
        return arq.readlines()
        #return arq.readlines().__len__()
        #return len(arq.readlines())

def escrever_arquivo(arquivo2:str, conteudo:list):
    '''função para escrever no arquivo'''
    try:
        with open(arquivo2, 'a') as arq2:
            arq2.writelines(conteudo)
    except Exception as e:
        print('Erro: {}'.format(e))

a = ler_arquivo('/home/developer/520/Aula-2/nomes.txt')
print(a)

b = '/home/developer/520/Aula-2/nomes5.txt'
c = escrever_arquivo(b,a)