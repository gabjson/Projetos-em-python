
'''

Descrição :
Crie um programa que receba como entrada um número natural n (n > 0)
e exiba os números não-primos que estão no intervalo fechado [ 1..n ].

'''

def qtd_divisores(n):
    qtd = 0
    for divisor in range(1, n+1):
        if n % divisor == 0:
            qtd += 1
    return qtd

def primo(n):
    return qtd_divisores(n) == 2

def intervalo_primos(a, b):
    for num in range(a, b+1):
        if not primo(num): print(num, end=' ')

n = int(input())
intervalo_primos(1, n)
