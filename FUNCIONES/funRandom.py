
import random

num_aleatorio = random.randint(0, 50)

num_usuario = int(input("Ingrese un numero: "))

while num_aleatorio != num_usuario:
    if num_usuario > num_aleatorio:
        print("Te pasaste, un poco mas abajo")
        num_usuario = int(input("Ingrese un numero: "))
    elif num_usuario < num_aleatorio:
        print("Te pasaste, un poco mas arriba")
        num_usuario = int(input("Ingrese un numero: "))

print("Adivinaste el numero, este era: ", num_aleatorio)
    



