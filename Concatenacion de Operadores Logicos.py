#edad=145

#if 0<edad<100:
	#print("La edad es Correcta")

#else:
	#print("Edad Incorrecta")


salario_presidente=int(input("Introduce salario presidente: "))
print("Salario Presidente:" + str( salario_presidente))

salario_director=int(input("Introduce salario Director: "))
print("Salario director:" + str( salario_director))

salario_administrativo=int(input("Introduce salario Administrativo: "))
print("Salario Administrativo:" + str( salario_administrativo))


salario_contador=int(input("Introduce salario contador: "))
print("Salario Contador:" + str( salario_contador))

if salario_administrativo<salario_director<salario_presidente:
	print("Todo funciona correctamente")

else:
	print("Algo huele mal en la empresa")
