"""

Descrição : 
Faça um programa que recebe o valor de três arestas (número inteiro)
e exibe uma mensagem indicando se podem formar um triângulo.]
Em caso afirmativo, indique se ele é equilátero, isósceles ou escaleno.
Lembre-se: Para que um triângulo exista, a medida de qualquer um dos lados deve ser menor que a soma das medidas dos outros dois
"""

N1 = int(input())
N2 = int(input())
N3 = int(input())

if N1 >= N2 + N3 or N2 >= N1 + N3 or N3 >= N1 + N2:
    print ('nao podem formar um triangulo')
    quit()
    
if N1 == N2 == N3:
    print ('podem formar um triangulo\nequilatero')
    quit()
elif N1 == N2 or N1 == N3 or N2 == N3:
    print ('podem formar um triangulo\nisosceles')
else:
    print ('podem formar um triangulo\nescaleno')
