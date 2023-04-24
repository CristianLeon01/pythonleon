
#Escribir un programa el cual solo permita numeros pares para salir del bucle.

while True:
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        print("El número ingresado es par. ¡Hasta luego!")
        break
    else:
        print("El número ingresado es impar. Intente de nuevo.")
