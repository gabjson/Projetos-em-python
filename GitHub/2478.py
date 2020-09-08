'''

[for] Desenvolva um programa que exibe a tabuada de um número natural escolhido pelo usuário.
Os múltiplos apresentados devem ser de 1 a 10.

'''
tabuada=int(input("Tabuada do numero: "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )
