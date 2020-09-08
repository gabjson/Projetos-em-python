# validação
valido = False
while not valido:
    n = int(input('n: '))
    if n >= 0 :
        valido = True

# Cont letters
cont = 1
while n >= 10 :
   n = n // 10
   cont += 1
print('A quantidade de  letters é:', cont)
        
