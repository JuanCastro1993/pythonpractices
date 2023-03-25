print("Verificacion de Edad : ")

edad_usuario = int(input("Introduce tu edad: "))

if edad_usuario<18:
	print("No puede pasar")

else:
	print("Puede Pasar")
print("El programa ha finalizado!")

# como hacer para poder validar varios ifs, para esto tenemos que crear varios elif.

nota_alumno = int(imput("Introduce tu nota, por favor: "))

if nota_alumno<5:
	print("Insuficiente")

elif nota_alumno<6:
	print("Suficiente")

elif nota_alumno<7:
	print("Bien")

elif nota_alumno<9:
	print("Notable")

else:
	print("Has sobresalido")
