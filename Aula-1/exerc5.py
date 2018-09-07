#!/usr/bin/python3
# 1. Dado a matriz, calcular a soma das diagonais
# matriz = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#exemplo = 1+5+9+3+5+7
linha1=[1,2,3]
linha2=[4,5,6]
linha3=[7,8,9]
matriz=[linha1,linha2,linha3]
result=matriz[0][0]+matriz[1][1]+matriz[2][2]+matriz[0][2]+matriz[1][1]+matriz[2][0]
print(result)