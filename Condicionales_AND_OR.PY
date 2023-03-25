print("Programa de becas 2023")
distancia_escuela=int(input("Introduce la distancia a la escuela en Km: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el No. de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario Anual: "))

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
	print("El Alumno merece beca")

else:
	print("El Alumno no tiene derecho a beca: ")