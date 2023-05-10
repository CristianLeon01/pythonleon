import random

# Genera un número aleatorio entre 0 y 50 y lo asigna a la variable "num_aleatorio"
num_aleatorio = random.randint(0, 50)

# Solicita al usuario que ingrese un número y lo convierte en entero
num_usuario = int(input("Ingrese un número: "))

# Bucle while que se ejecuta mientras el número ingresado no sea igual al número aleatorio
while num_aleatorio != num_usuario:
    # Si el número ingresado es mayor al número aleatorio, indica al usuario que ingrese un número más bajo
    if num_usuario > num_aleatorio:
        print("Te pasaste, un poco más abajo")
        num_usuario = int(input("Ingrese un número: "))
    # Si el número ingresado es menor al número aleatorio, indica al usuario que ingrese un número más alto
    elif num_usuario < num_aleatorio:
        print("Te pasaste, un poco más arriba")
        num_usuario = int(input("Ingrese un número: "))

# Cuando el número ingresado es igual al número aleatorio, se imprime un mensaje indicando que se adivinó el número
print("Adivinaste el número, este era: ", num_aleatorio)

    



