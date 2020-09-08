'''
Uma empresa quer aumentar suas vendas e para isso divulgou promoções com descontos atrelados às formas de pagamento.
Os produtos com desconto terão uma etiqueta em que constam o preço normal (PN) e o preço promocional (PP).
De acordo com a porcentagem de desconto entre PN e PP, a empresa indicará a forma de pagamento aceita.
Caso o desconto seja > 30%, o pagamento será à vista em dinheiro;
caso o desconto esteja entre ]20%,30%] o pagamento será à vista com cartão de crédito; caso o desconto seja ≤ 20%, o pagamento será parcelado com cartão de crédito.
Crie um PROGRAMA que receba como entrada PN e PP e exiba a forma de pagamento aceita. O programa deve funcionar idêntico ao ilustrado nas figuras.
'''
pn = float(input('Preço Normal: '))
pp = float(input('Preço Promocional: '))
desconto = pn - pp

if desconto > pn * 0.3:
    pay = 'Dinheiro'
elif desconto > pn * 0.2:
    pay = 'Crédito à vista'
else:
    pay ='Crédito Parcelado'
print(pay)
