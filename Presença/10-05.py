'''criando uma lista'''
lista_compras = ['cereal', 'leite', 'banana', 'maçã', 'iogurte']
n = len(lista_compras)
print('Número de itens: ', n)

''' Substituindo um valor '''
lista_compras = ['cereal', 'leite', 'banana', 'maçã', 'iogurte']
print('Antes:', lista_compras)
lista_compras[3] = 'mamão'
print('Depois:', lista_compras)

''' Inserindo um valor '''

lista_compras = ['cereal', 'leite', 'banana', 'mamão', 'iogurte']
print('Antes:', lista_compras)
lista_compras.insert(4, 'melão')
print('Depois:', lista_compras)

''' Removendo um valor '''
lista_compras = ['cereal', 'leite', 'banana', 'mamão', 'melão', 'iogurte']
print('Antes:', lista_compras)
del lista_compras[1]
print('Depois:', lista_compras)

''' Acresentar um valor no final da lista '''
lista_compras = ['cereal', 'banana', 'mamão', 'melão', 'iogurte']
print('Antes:', lista_compras)
lista_compras.append('mel')
print('Depois:', lista_compras)

''' Alterando a posição de um valor '''
lista_compras = ['cereal', 'banana', 'mamão', 'melão', 'iogurte', 'mel']
print('Antes:', lista_compras)
lista_compras.sort()
print('Depois:', lista_compras)

''' Invertendo a posição de um valor '''
lista_compras = ['cereal', 'banana', 'mamão', 'melão', 'iogurte', 'mel']
print('Antes:', lista_compras)
lista_compras.reverse()
print('Depois:', lista_compras)
