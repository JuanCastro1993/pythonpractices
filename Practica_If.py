print("Evaluacion de Alumnos")

nota_alumno=input("Introduzca la Nota del Alumno: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion



print (evaluacion(int(nota_alumno)))