import math


def calculaRaiz(num1):
	if num1<0:
		raise ValueError("El numero no puede ser negativo")
	else:
		return math.sqrt(num1)


op1=(int(input ("Introduce un Numero: ")))

try:
	print(calculaRaiz(op1))

except ValueError as ErrordeNumeroNegativo:
	print(ErrordeNumeroNegativo)

print("programa terminado")