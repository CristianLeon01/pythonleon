#Escribir un programa el cual solo permita numeros pares para salir del bucle.

#se usa el bucle while para mantener un ciclo
while True:
    num = int(input("Ingrese un número: "))

    #se utiliza el condicional if para poner la condicion de que solo se puede ingresar numeros pares.
    if num % 2 == 0:
        print("El número ingresado es par. ¡Hasta luego!")
        break
    else:
        print("El número ingresado es impar. Intente de nuevo.")
