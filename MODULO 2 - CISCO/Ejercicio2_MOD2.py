
#Imprimir en pantalla la diferencia en años de la edad de 2 personas.

#Se le solicita al usuario 2 edades.
edad1 = int(input("Digite la edad de la persona 1: "))
edad2 = int(input("Digite la edad de la persona 2: "))

#Se realiza una operacion de resta entre las 2 edades donde el resultado se almacenara en una nueva variable.
edad_total = (edad1 - edad2)

#Se imprime la diferencia de edades.
print("La diferencia en años de edad entre ambas personas es de:", edad_total, "años")