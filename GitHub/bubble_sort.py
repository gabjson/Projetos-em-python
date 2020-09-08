def exibe(v, n):
    for i in range(n):
        print(v[i], end=' ')
    print()

def preenche(v, n):
    for i in range(n):
        v[i] = int(input('vetor[%d]: ' % i))

def troca(v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp
'''
def troca(v, i, j):
    v[i], v[j] = v[j], v[i]
'''
def empurra(v, n):
    i = 0
    while i < n-1:
        if v[i] > v[i+1]:
            troca(v, i, i+1)
        i += 1
'''
def empurra(v, n):
    for i in range(n-1):
        if v[i] > v[i+1]:
            troca(v, i, i+1)
'''
def bubble_sort(v, n):
    tam = n
    while tam > 1:
        empurra(v, tam)
        tam -= 1
'''
def bubble_sort(v, n):
    for tam in range(n, 1, -1):
        empurra(v, tam)
'''

v = [40,20,50,30,10]
exibe(v, 5)
bubble_sort(v, 5)
exibe(v, 5)
