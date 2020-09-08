'''
Descrição :

Crie um programa que receba como entrada um caractere alfabético maiúsculo e exiba
a sequência do alfabeto maiúsculo de 'A' até o caractere lido.
O programa deverá repetir o procedimento até que seja dado como entrada o caractere 'F'.

'''


def ler_letras():
    while True:
        letra = input()
        if len(letra) == 1 and 'A' <= letra <= 'Z':
            return letra

while True:
    letra = input()
    if letra == 'F':
        break
    for i in range(65, ord(letra) + 1):
        print(chr(i), end=' ')
    print()
