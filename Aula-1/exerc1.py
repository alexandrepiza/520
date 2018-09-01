#!/usr/bin/python3
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2
if media >= 7:
    print('Média: '.format(media))
    print('Aprovado')
elif media<=3:
    print('Média: ',format(media))
    print('Reprovado')
else:
    print('Média: ',format(media))
    print('Recuperação')