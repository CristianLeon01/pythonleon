
#Escribir un programa el cual solicite dos nombres y sus edades y decir cual de los 2 es mayor.

nom1 = input("Digite el nombre de la Primera persona: ")
edad1 = input("Digite la edad de la Primera persona: ")

nom2 = input("Digite el nombre de la Segunda persona: ")
edad2 = input("Digite la edad de la Segunda persona: ")

if edad1 > edad2:
    print(nom1, "es mayor que", nom2)

elif edad2 > edad1:
    print(nom2, "es mayor que", nom1)

else:
    print("Las 2 perosnas tiene la misma edad")
