#si el numero es par saquen la raiz cuadrada si en numero impar elevarlo al cuadradoo
import random 
import math 

tam = random.randint(5, 10)

lista =[random.randrange (100) for i in range (tam)]
lista_2 = [round(math.sqrt(numero), 2) if numero % 2 == 0 else numero ** 2 for numero in lista]

print("Lista original:", lista)
print("Lista modificada:", lista_2)