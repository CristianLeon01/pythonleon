from random import randint 
import math

# Inicialización de variables
suma = 0
mayor = 0
menor = 50
moda = 0
resta = 0
desviacion_estandar = 0

# Generación de lista aleatoria de 5 números enteros entre 1 y 20
lista_numeros = [randint(1,20) for i in range(0,5)]
print (lista_numeros)

# Suma de los números
for i in lista_numeros:
    suma = suma + i
print("la suma de los numero de la lista es de :", suma)

# Búsqueda del número mayor y menor
for i in lista_numeros:
    if i > mayor:
        mayor = i
    if i < menor:
        menor = i

print("El numero mayor de la lista es:", mayor)
print("El numero menor de la lista es:", menor)

# Cálculo de la media
media = suma / len(lista_numeros)
print("Media de los números:", media)

# Cálculo del promedio
promedio = suma / len(lista_numeros)
print("El promedio de los números de la lista es: ", promedio)

# Cálculo de la desviación estándar
for numero in lista_numeros:
    desviacion_estandar += (numero - media) ** 2
desviacion_estandar /= len(lista_numeros)
desviacion_estandar = math.sqrt(desviacion_estandar)

print("Desviación estándar de los números:", desviacion_estandar)
