"""

Descrição : 
A Locadora de Veículos Eudora lançou uma grande promoção esse mês: pagando apenas R$ 90 por diária, o cliente pode alugar um carro de passeio. Para cada diária,
o cliente recebe uma cota de quilometragem de 100 Km.
Cada quilômetro a mais custará uma taxa extra de R$ 12.

Escreva um programa que receba como entrada a quantidade de dias e a quilometragem total rodada por um cliente dessa locadora e exiba o valor total a ser pago com duas casas decimais.
"""

dia = int(input())
km = int(input())

cota = 100
diaria = dia * 90

if km <= cota :
    preco = 0
else:
    preco=(km-(cota*dia))*12

print("%.2f" %((diaria)+ preco))
