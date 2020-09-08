'''
A escola de Joãozinho tradicionalmente organiza uma corrida ao redor do prédio. Como todos os alunos são
convidados a participar e eles estudam em períodos diferentes, é difícil que todos corram ao mesmo tempo.

Para contornar esse problema, os professores cronometram o tempo que cada aluno demora para dar cada volta
ao redor da escola, e depois comparam os tempos para descobrir a classificação final.

Sua tarefa é, sabendo o número de competidores, o número de voltas de que consistiu a corrida e os tempos
de cada aluno competidor, descobrir quem foi o aluno vencedor, para que ele possa receber uma medalha
comemorativa.
'''

def converte(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    return lista

def soma(lista):
    s = 0
    for i in range(len(lista)):
        s += lista[i]
    return s

N, M = input().split()
N = int(N)
M = int(M)
menor = 1000000 * 101 # dá para melhorar
for i in range(1, N+1):
    voltas = input().split()
    voltas = converte(voltas)
    total = soma(voltas)
    if total < menor:
        menor = total
        competidor = i
print(competidor)
