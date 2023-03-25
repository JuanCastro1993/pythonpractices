def sum_or_mult(number1, number2):
	product = number1 * number2


	if product <=1000:
		return product

	else:
		return number1 + number2

resultado = sum_or_mult (20,40)
print("El Resultado es: ", resultado)
