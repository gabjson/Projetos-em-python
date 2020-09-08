"""

Descrição : 
Na empresa em que você trabalha há muitos funcionários,
e às vezes o depósito do INSS é feito incorretamente para alguns deles pois é um processo manual e portanto sujeito a erros.
Com isso você decidiu propor a automação de tal processo, para torná-lo mais rápido e reduzir a chance de erros.
Escreva um programa que receba o salário base de um funcionário e calcule qual a contribuição devida ao INSS,
dada de acordo com a seguinte tabela:

"""

salario = float(input())

if salario <= 1757.81:
    contribuicao = salario * 0.08
elif salario <= 2919.72:
     contribuicao = salario * 0.09
elif salario <= 5839.45:
     contribuicao = salario * 0.11
else:
     contribuicao = 5839.45 * 0.11
     
print('Desconto do INSS: R$ %.2f' % contribuicao)
