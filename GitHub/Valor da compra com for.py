'''

Crie um programa que receba como entrada a quantidade de produtos que um consumidor comprou em um shopping
o Pograma deverá solicitar o valor de cada produto,somar os valores e exibir o total

'''

qtd = int(input('Quantidade : '))
soma = 0

for cont in range(qtd) :
    preco = float(input('Preço : '))
    soma += preco
print('o total é : R$ %.2f' % soma)
