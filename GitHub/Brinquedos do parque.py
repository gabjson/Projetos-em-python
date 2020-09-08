"""
Descrição : 
Nos parques de diversão, alguns brinquedos tem idade e altura mínimas para poder andar neles.

O parque Ambrolândia possui 3 brinquedos que possuem essa limitação:

Barca Viking: 1,5m de altura e 12 anos.

Elevator of Death: 1,4m de altura e 14 anos.

Final Killer: 1,7m de altura ou 16 anos. 

Dada a altura e a idade de uma pessoa,
faça um programa que identifique quantos brinquedos ele pode andar.

formato de entrada :
Dois inteiros, F e I, representando a altura (em cm) e a idade, respectivamente.
"""

F,I = input().split(' ')

F = int(F)
I = int(I)
G = 0

if F >= 150 and I >= 12:
    G = G + 1
if F >= 140 and I >= 14:
    G = G + 1 
if F >= 170 or I >= 16:
    G = G + 1

print(G)

