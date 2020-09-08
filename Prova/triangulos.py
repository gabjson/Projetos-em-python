N1 = int(input('n1 :'))
N2 = int(input('n2 :'))
N3 = int(input('n3 :'))


if N1 >= N2 + N3 or N2 >= N1 + N3 or N3 >= N1 + N2:
    print ('nao podem formar um triangulo')
    quit()
    
if N1 == N2 == N3:
    print ('podem formar um triangulo\nequilatero')
    quit()
elif N1 == N2 or N1 == N3 or N2 == N3:
    print ('podem formar um triangulo\nisosceles')
else:
    print ('podem formar um triangulo\nescaleno')
