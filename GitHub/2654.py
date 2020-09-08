'''
Descrição :
Faça um programa que preenche um vetor com cinquenta elementos inteiros e altera todo valor negativo para seu oposto positivo, ao final o programa deve exibir o vetor já modificado.
'''

arr = []

for count in range(50) :
    arr.append(int(input()))

arr = list(map(abs, arr[0:50]))

for i in range(50) :
    print(arr[i])
  
