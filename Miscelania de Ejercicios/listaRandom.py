#Imprimir la suma, el promedio, el numero mayor, el numero menor...
#La moda, la mediana y la desviacion extandar de una lista aleatoria.
import math
import random

# Se declaran algunas variables con valores iniciales.
sum=0
prom=0
mayor=0
menor=101
moda=0
resta=0
division=0
raiz=0
moda=0
mediana=0

# Se crea una lista vacía y se genera un número aleatorio que se usará como el tamaño de la lista.
lista=[]
tam=random.randint(10,20)

# Se agrega un número aleatorio entre 0 y 100 a la lista para cada iteración del ciclo for.
for i in range (tam):
    num=random.randrange(100)
    lista.append(num)
    
# Se muestra la lista.
print (f'En la lista hay {tam} elementos: ')
print(lista)
print()

# Se calcula la suma de todos los números en la lista.
for numeros in lista:
    sum += numeros
print (f'La suma total es: {sum}')

# Se calcula el promedio de los números en la lista.
for numeros in lista:
    prom = sum//tam
print (f'El promedio es: {prom}')

# Se encuentra el número mayor y el número menor en la lista.
for numeros in lista:
    if numeros>mayor:
        mayor=numeros
    if numeros<menor:
        menor=numeros
print(f'El numero mayor es: {mayor} ')
print(f'El numero menor es: {menor} ')

# Se encuentra la mediana de los números en la lista.
if tam % 2 == 0:
     num1 = tam // 2
     num2 = num1 -1
     mediana = (lista[num1]+lista[num2]) // 2
     print(f'La mediana es: {mediana}')
else:
    num_imp = tam // 2
    mediana = (lista[num_imp])
    print(f'La mediana es: {mediana}')

# Se encuentra la moda de los números en la lista.
max = 0
for num in lista:
    cont = 0
    for s in lista:
        if num == s:
            cont +=1
    if cont > max:
        max = cont
        moda =num
print (f'La moda es: {moda}')

# Se calcula la desviación estándar de los números en la lista.
for numeros in lista:
     numeros = resta - (sum) / (prom)
     cuadrado = resta ** 2
     sum += cuadrado
     division = sum / prom
raiz = math.sqrt (division)
print(f'La desviacion extandar es: {raiz} ')

# Se ordena la lista en orden ascendente.
for i in range(tam-1):
    for j in range(i+1,tam):
        if lista[i]>lista[j]:
            lista[i],lista[j]=lista[j],lista[i]
print('El orden de la lista de menor a mayor es:')
print (lista)
print()

# Se ordena la lista en orden descendente.
for i in range(tam-1):
    for j in range(i+1,tam):
        if lista[i]<lista[j]:
            lista[i],lista[j]=lista[j],lista[i]
print('El orden de la lista de mayor a menor es: ')
print (lista)
