'''
Crie uma FUNÇÃO que receba como parâmetro uma tupla T de números naturais e devolva uma lista com apenas os itens de T
que possuam no mínimo três dígitos e na mesma ordem em que estão em T.
Exemplo: se T=(156,9,7854,0,123,74,25), a lista devolvida será [156,7854,123].
Restrições:
(I) só um loop;
(II) funções/métodos permitidos: append(), len() e range();
(III) só recursos dados em aula.
'''
def tuplas(t):
    l = []
    for count in range(len(t)):
        if t[count] >= 100:
            l.append(t[count])
    return l
