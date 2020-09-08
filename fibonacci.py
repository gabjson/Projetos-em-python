'''

Descrição :
Crie um programa que tenha apenas uma função, além do programa principal,
que receberá como parâmetros um número natural estritamente positivo n e que exiba os n primeiros elementos da Sequência de Fibonacci.
O PROGRAMA PRINCIPAL deverá ler o valor n e chamar a FUNÇÃO que, por sua vez, exibirá os elementos.


'''

def fibonacci_loop(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    elif num > 2:
        a = 1 # variable for (n - 1)
        b = 1 # variable for (n - 2)
        for _ in range(3, num + 1):
            c = a + b
            a, b = b, c

        return c
