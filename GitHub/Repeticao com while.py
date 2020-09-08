'''Og é um homem das cavernas com vários filhos e filhas, e ele quer contar todos eles.
Og conta seus filhos com sua mão esquerda e suas filhas com sua mão direita.

Entretanto, Og não é inteligente, e não sabe somar os dois números.
Assim, ele pediu para você escrever um programa que realize a soma.'''


L, R = input().split()
L, R = int(L), int(R)

while L != 0 or R != 0 :
    print(L + R)
    L, R = input().split()
    L, R = int(L), int(R)
