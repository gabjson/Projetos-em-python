'''
Crie um PROGRAMA que receba como entrada um natural n (n>0) e exiba a soma dos n primeiros naturais pares. Exemplo: se n=6, será exibido 30, a soma de 0+2+4+6+8+10.
Restrições: (I) só um loop; (II) sem listas; (III) funções/métodos permitidos: input(), int(), print() e range(); (IV) só recursos dados em aula.
'''

n = int(input('Digite o numero : '))
soma = 0
for count in range(0,n*2,2) :
    soma += count
print(soma)
            
