# Se importa la librería random
import random

# Se crean dos listas vacías para almacenar los números aleatorios y sus cuadrados
lista=[]
cuadrado=[]

# Se genera un número aleatorio entre 5 y 10 para determinar el tamaño de la lista
tam=random.randint(5,10)
print(tam)

# Se llena la lista con números aleatorios
for i in range(tam):
    num=random.randrange(100)
    lista.append(num)
print(lista)

# Se calculan los cuadrados de los elementos de la lista y se almacenan en la lista cuadrado
for i in range(len(lista)):
    cuadrado.append(lista[i]**2)

# Se imprime la lista de cuadrados
print(cuadrado)

# Se calcula la suma de todos los elementos en la lista original y se imprime el resultado
print(sum(lista))
