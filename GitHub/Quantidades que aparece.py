'''

Descrição :
Dado um número Y, imprima quantas vezes Y aparece em uma sequência.

Formato de entrada :

2 números X,Y onde X indica a quantidade de números da sequência e Y o número procurado.

uma sequência de X números.

'''

x = int(input('Quantidade'))
y = int(input('Numero'))quant = 0

for count in range (x) :
    x = int(input('Quantidade'))
    if x == y :
        quant += 1
print(quant)
        
