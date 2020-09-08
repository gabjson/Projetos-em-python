''' Utilizando o operador while [while] Faça um programa que recebe valores inteiros positivos até que seja digitado o valor zero,
que não deverá ser contabilizado. O programa deverá exibir o maior valor lido.

Formato de entrada :

Diversos valores inteiros positivos, um por linha. A entrada é encerrada com a leitura do valor zero (que não deve ser contabilizado).

Formato de saída :

O maior valor lido.


'''

a = float(input())
maior = a
while a != 0 :
    if a > maior :
        maior = a
        a = int(input())
print(maior)
