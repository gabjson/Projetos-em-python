#Entrada
Media,nAulas,nFaltas = input().split(" ")

#Transformando as variáveis de "String" para "Float" e "Int"
Media = float(Media)nAulas = int(nAulas)nFaltas = int(nFaltas)

#Cálculo
frequencia = (((nAulas - nFaltas)/ nAulas) * 100)

#Condição
if (frequencia >= 75 and Media >= 5) or (frequencia >= 50 and Media >= 7):                     print("Aprovado")
else:   
    print("Reprovado")

Leia mais em Brainly.com.br - https://brainly.com.br/tarefa/10597541#readmore
