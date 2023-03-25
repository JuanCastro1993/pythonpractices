#i=1

#while i<=10:
    #print("Ejecucion " + str(i))
    #i=i+1

#print("Termino la Ejecucion")

edad=int(input("Introduce la edad por favor: "))

while edad<0:
    print("Has Introducido una edad incorrecta. Vuelve a Intentarlo")
    edad=int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar. Puedes Pasar")
print("Gracias por colaborar no cumples con la edad" + str(edad))
