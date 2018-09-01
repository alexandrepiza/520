#!/usr/bin/python3
i=int(0)
#print(i)
lista=[i]
for i in range(0,100,2): #No python o 1º num é inclusivo e o segundo é exclusivo, então neste caso deconta de 0 a 99
    i+=2
    lista.append(i)
print('lista: ',lista,end='\n\n')

#ou

lista2=[]
for i in range(0,101,2):
    lista2.append(i)
print('lista2: ',lista2)