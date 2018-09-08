#!/usr/bin/python3
print('Forma 1')
arquivo = open('/home/developer/520/Aula-2/nomes.txt','r')

print(arquivo.read(),end='\n\n')

arquivo.close()

# Segunda forma
print('\nForma 2')
with open('/home/developer/520/Aula-2/nomes.txt','r') as arquivo:
    print(arquivo.read())

print('\nForma 3')
with open('/home/developer/520/Aula-2/nomes.txt','r') as arquivo:
    print(arquivo.readlines())

print('\nForma 4')
with open('/home/developer/520/Aula-2/nomes.txt','a+') as arquivo:
    arquivo.write('\njose')
    arquivo.write('\nrodolfo')
    arquivo.seek(0)

#with open('/home/developer/520/Aula-2/nomes.txt','r') as arquivo:
    # print(arquivo.read())
