'''
Marianna e Marinna são amigas e conversam bastante sobre muitos segredos.
Para que as demais pessoas não lessem suas conversas criaram um código entre elas.
O código estabelece uma relação entre letras e números conforme mostrado abaixo.
Faça uma função chamada "traduzir", que recebe uma uma mensagem e retorna a mensagem traduzida.
'''


def converte(codigo) :
    for i in range(len(codigo)) :
        codigo[i] = int(codigo[i])
    return codigo
        
def traduz(codigo):
    codigo = converte(codigo)
    frase = ''
    for i in range(len(codigo)) :
        if codigo[i] != 0:
            frase += chr(codigo[i] + 96)
        else:
            frase +=' '
    return frase

codigo = (input()).split()
frase = traduz(codigo)
while frase != 'fim' :
    print(frase)
    codigo = input().split()
    frase = traduz(codigo)
