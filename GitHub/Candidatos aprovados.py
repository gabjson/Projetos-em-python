
'''
Descrição :

O IBGE realizou um concurso para contratar pessoas para trabalhar no censo. Cada candidato fez uma prova de português com 50 questões,
outra de matemática com 35 questões, e uma prova de redação.

Para ser aprovado, era necessário acertar pelo menos 80% da prova de português, 60% da prova de matemática, e ter nota igual ou superior a 7 na redação.

Escreva um programa que receba como entrada, para cada candidato, a quantidade de questões certas em português e em matemática,
e também a nota na redação, e depois exiba quantos candidatos foram aprovados.

Formato de entrada :

Dois números inteiros seguidos por um número real para cada candidato

A entrada deve encerrar quando a quantidade de questões de português informada for inferior a zero


'''

quant = 0
port = int(input('Prova de portugues : '))
       
while port > 0 :
    math = int(input('Prova de matematica : '))
    red = float(input('Redação : '))
    if port >= 40 and math >= 21 and red >= 7.0 :
        quant += 1
    port = int(input('Prova de portugues : '))
print('Candidatos aprovados:', quant)
        
              

