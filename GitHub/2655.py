'''
Descrição :
Faça um programa que lê um vetor de cinquenta números inteiros e exibe,
ao final, o menor valor lido.
'''

arr = []

for count in range(50) :
    arr.append(int(input()))
    
print(min(arr))


'''
if len(arr) > 1:
      if arr[cont] < min :
           min = arr[cont]
else:
       min = arr[cont]
'''
