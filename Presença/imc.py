 
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
 
imc = peso /((altura/100)**2)
 
print("Seu IMC é: %.4f" % imc)
 
if imc < 20:
	print("Abaixo do peso")
elif imc <= 20 or imc <= 25 :
	print("Normal")
elif imc < 25 or imc <= 30:
	print("Excesso de peso")
elif imc < 30 or imc <= 35:
	print("Obesidade")
elif  imc < 35:
	print("obesidade mordbida")
