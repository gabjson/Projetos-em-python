"""

Descrição : 
Faça um programa que leia um caractere da entrada padrão e
verifique se ele é uma vogal.
Se o usuário digitar mais ou menos de 1 caractere, exiba uma mensagem de erro.
"""

l=input()

if l=='a' or l=='e' or l=='i' or l=='o' or l=='u' or l=='A' or l=='E' or l=='I' or l=='O' or l=='U':
    print('Eh vogal')
elif len(l) > 1:
    print('1 caractere, por favor!')
else:
    print('Nao eh vogal')
