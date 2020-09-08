"""

Descrição : 
Escreva um programa que a partir da média, do número de aulas e faltas do aluno, defina seu resultado na disciplina. Os resultados possíveis são: APROVADO e REPROVADO. Para ser considerado APROVADO, o aluno precisa se enquadrar em uma das seguintes situações:

a) Frequência maior ou igual 75% com média maior ou igual a 5;

b) Frequência maior ou igual a 50% caso a média seja maior ou igual a 7.

Caso não se enquadre em pelo menos uma delas, é considerado REPROVADO.
"""

media, aulas, faltas = input().split(" ")

media = float(media)
aulas = int(aulas)
faltas = int(faltas)

frequencia = (((aulas - faltas)/ aulas) * 100)

if (frequencia >= 75 and media >= 5) or (frequencia >= 50 and media >= 7):
    print('APROVADO')
else:   
    print('REPROVADO')
