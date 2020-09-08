frase = input('frase: ')
palavra = input('palavra: ')

qtd_ocorrencias = frase.count(palavra)

p = frase.index(palavra)
print('Posição: ', p)

for i in range(qtd_ocorrencias-1) :
    p = frase[p + 1] .index(palavra) + (p + 1)
    print('Posição :', p)
