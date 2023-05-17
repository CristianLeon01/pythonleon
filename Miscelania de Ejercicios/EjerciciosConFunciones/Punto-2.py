import random

# Función para llenar una lista con números aleatorios dentro de un rango dado
def llenarLista(tam, rango):
    lista = []
    lista = [random.randrange(rango) for i in range(tam)]
    return lista

# Crear dos listas con números aleatorios
l1 = llenarLista(15, 100)
l2 = llenarLista(15, 100)

print("La lista Numero 1 es la siguiente:", l1)
print("La lista Numero 2 es la siguiente:", l2)
print()


# Función para calcular la suma de los elementos de una lista
def suma_lista(lista):
    sum = 0
    for x in lista:
        sum += x
    return sum

print("La Suma Lista N1 es la siguiente:", suma_lista(l1))
print("La Suma Lista N2 es la siguiente:", suma_lista(l2))
print()


# Función para determinar cuál de las dos listas tiene una suma mayor
def mayor_suma():
    suma = 0
    if suma_lista(l1) > suma_lista(l2):
        suma = "Lista 1", suma_lista(l1)
    else:
        suma = "Lista 2", suma_lista(l2)
    return suma


# Función para encontrar el número mayor entre las dos listas
def num_mayor():
    mayor = 0
    for i in l1 and l2:
        if i > mayor:
            mayor = i
    return mayor


# Función para encontrar el número menor entre las dos listas
def num_menor():
    menor = 100000
    for i in l1 and l2:
        if i < menor:
            menor = i
    return menor


# Función para calcular el promedio del conjunto de las dos listas
def prom_conjunto():
    prom = (suma_lista(l1) + suma_lista(l2)) / 2
    return prom


# Función para calcular el promedio de una lista dada
def promedioLista(lista):
    return suma_lista(lista) / len(lista)


# Función para determinar si el promedio de una lista es mayor que el promedio del conjunto
def pro_may_men():
    if promedioLista(l1) > prom_conjunto():
        return "La lista N1 es mayor al promedio del conjunto", promedioLista(l1)
    elif promedioLista(l2) > prom_conjunto():
        return "La lista N2 es mayor al promedio del conjunto", promedioLista(l2)
    else:
        return "Los dos promedios estan por debajo del promedio conjunto:", prom_conjunto()


# Función para contar la cantidad de números pares en una lista
def contar_pares(lista):
    cont_pares = 0
    for numero in lista:
        if numero % 2 == 0:
            cont_pares += 1
    return cont_pares


# Función para contar la cantidad de números impares en una lista
def contar_impares(lista):
    cont_impares = 0
    for numero in lista:
        if numero % 2 != 0:
            cont_impares += 1
    return cont_impares


# Función para saber la mayor cantidad de pares
def mayorpar():
    may_pares = 0
    if contar_pares(l1) > contar_pares(l2):
        may_pares = "Lista N1",contar_pares(l1)
    else:
        may_pares = "Lista N2",contar_pares(l2)
    return  may_pares


# Función para saber la mayor cantidad de impares
def mayorimpar():
    may_impares = 0
    if contar_impares(l1) > contar_impares(l2):
        may_impares = "Lista N1",contar_impares(l1)
    else:
        may_impares = "Lista N2",contar_impares(l2)
    return  may_impares


print("El resultado mayor de la Suma de las dos Listas es la:", mayor_suma())
print()
print("El numero mayor de las 2 Listas es:",num_mayor())
print("El numero menor de las 2 Listas es:",num_menor())
print()
print("El promedio del conjunto es:",prom_conjunto())
print()
print("El promedio de la lista N1 es:",promedioLista(l1))
print("El promedio de la lista N2 es:",promedioLista(l2))
print()
print(pro_may_men())
print()
print(f"En la lista N1 hay: {contar_pares(l1)} numeros pares")
print(f"En la lista N2 hay: {contar_pares(l2)} numeros pares")
print()
print(f"En la lista N1 hay: {contar_impares(l1)} numeros impares")
print(f"En la lista N2 hay: {contar_impares(l2)} numeros impares")
print()
print("La lista que tiene mas pares es la:",mayorpar())
print("La lista que tiene mas impares es la:",mayorimpar())
print()
