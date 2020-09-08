import random

def aleatorio(i, f):
    return random.randint(i, f)

def preenche(v, n) :
    for i in range(n) :
        v[i] = aleatorio(10, 99)

def exibe(v, n) :
    for i in range(n) :
        print(v[i], end=' ')
    print()

n = 10
v = n * [0]
preenche(v, n)
exibe(v, n)
