#!/usr/bin/python3
mensagem='Digite somente numeros!'
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
for x in range (qtnotas):
    try:
        #print('Digite a nota', x+1,': ')
        nota = float(input('Digite a nota {}: '.format(x+1)))
        if nota > 10:
            print('nota inválida')
            qtnotas -= 1
            continue
        total += nota
    except Exception as er:
        print(er)
        print(mensagem)
        exit()

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