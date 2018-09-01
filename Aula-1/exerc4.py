#!/usr/bin/python3
letras = []
for x in range(97, 123):
    letras.append(chr(x))

print(letras)

while letras:
    print(letras.pop(0))

print(letras, end=)