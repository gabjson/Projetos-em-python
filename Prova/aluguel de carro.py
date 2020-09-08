dia = int(input('dia'))
km = int(input('km'))

cota = 100
diaria = dia * 90

if km <= cota :
    preco = 0
else:
    preco=(km-(cota*dia))*12

print("%.2f" %((diaria)+ preco))
