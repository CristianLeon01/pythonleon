
#Escribir un programa el cual solicite dos nombres y sus edades y decir cual de los 2 es mayor.

#se asignan 4 variables en la cual el usuario digitara 2 nombre y 2 edades
nom1 = input("Digite el nombre de la Primera persona: ")
edad1 = input("Digite la edad de la Primera persona: ")

nom2 = input("Digite el nombre de la Segunda persona: ")
edad2 = input("Digite la edad de la Segunda persona: ")

#se utiliza la condicion if y elif para realizar condiciones entre las 2 edades.
if edad1 > edad2:
    print(nom1, "es mayor que", nom2)

elif edad2 > edad1:
    print(nom2, "es mayor que", nom1)

else:
    print("Las 2 perosnas tiene la misma edad")
