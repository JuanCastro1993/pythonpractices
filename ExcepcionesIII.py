def evaluaEdad (edad):
	if edad<0:
		raise TypeError("No se permiten edades Negativas")

	if edad<20:
		return "Eres Joven, Haaaa"
	elif edad<40:
		return "Eres un Joven Mayor"
	elif edad<60:
		return "Eres un Adulto"

	elif edad<100:
		return "Cuidate.."

print(evaluaEdad(15))

