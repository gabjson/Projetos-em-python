salario = float(input('salario :'))

if salario <= 1757.81:
    contribuicao = salario * 0.08
elif salario <= 2919.72:
     contribuicao = salario * 0.09
elif salario <= 5839.45:
     contribuicao = salario * 0.11
else:
     contribuicao = 5839.45 * 0.11
print('Desconto: R$ %.2f' % contribuicao)
