''''

Crie um programa que receba como entrada dois números naturais, A e B (A >= B), e exiba todos os números inteiros do intervalo aberto decrescente ]
A .. B [, ou seja, A e B não devem ser exibidos.

'''

A = int(input('a : '))
B = int(input('b : '))

A = A - 1
B = B + 1

while A >= B :
    print(A)
    A = A - 1

    

