def preenche(v, n) :
    for i in tange(n) :
        v[i] = int(input())

def indice(x, v, n) :
    for i in range(n) :
        if v[i]==x:
            return i
    return -1

tamanho = int(input())
a = tamanho * [0]
preenche(a, tamanho)
procurado = int(input())
ind = indice(procurado, a, tamanho)
if ind != -1 :
    print(ind)
else :
    print('N/a')
