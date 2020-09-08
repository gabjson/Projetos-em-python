"""

Descrição : 
Faça um pro grama que exibe quantos litros de combustível
são gastos por um carro em um dado percurso.
Serão fornecidos pelo usuário a distância percorrida (em km) e a quantidade de litros gastos por km.
"""

distancia = int(input())
km = float(input())

litros = distancia * km
print('%.2f' % (litros))
