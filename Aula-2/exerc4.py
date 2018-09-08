#!/usr/bin/python3
mensagem='Digite somente numeros! Tente novamente.'
x = 1
#while er = null:
try:
    qtnotas = int(input('Digite quantidade de notas: '))
except ValueError as er:
    print(er)
    print(mensagem)
    exit()
except Exception as er:
    print(er)
    pass

total = float(0)
while x <= qtnotas:
    try:
        #print('Digite a nota', x+1,': ')
        nota = float(input('Digite a nota {}: '.format(x)))
        if nota > 10:
            print('nota inválida')
            qtnotas -= 1
        total += nota
        x += 1
    except Exception as er:
        print(er)
        print(mensagem)

media = total/qtnotas
if media >= 7:
    print('Média: ',format(media))
    print('Aprovado')
elif media<=3:
    print('Média: ',format(media))
    print('Reprovado')
else:
    print('Média: ',format(media))
    print('Recuperação')