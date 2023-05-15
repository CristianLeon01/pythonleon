import random

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

l1 = llenarLista(15,100)
l2 = llenarLista(15,100)

print("La lista Numero 1 es la siguiente:",l1)
print("La lista Numero 2 es la siguiente:",l2)
print()

def suma_lista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

print("La Suma Lista N1 es la siguiente:",suma_lista(l1))
print("La Suma Lista N2 es la siguiente:",suma_lista(l2))
print()

def mayor_suma():
    suma=0
    if suma_lista(l1) > suma_lista(l2):
        suma = "Lista 1", suma_lista(l1)
    else:
        suma = "Lista 2", suma_lista(l2)
    return suma


def num_mayor():
    mayor = 0
    for i in l1 and l2:
        if i > mayor:
            mayor = i
    return mayor


def num_menor():
    menor = 100000
    for i in l1 and l2:
        if i < menor:
            menor = i
    return menor


def prom_conjunto():
    prom = (suma_lista(l1) + suma_lista(l2)) / 2
    return prom


def promedioLista(lista):
    return suma_lista(lista)/len(lista)


def pro_may_men():
    if promedioLista(l1) > prom_conjunto():
        return "La lista N1 es mayor al promedio del conjunto",promedioLista(l1)
    elif promedioLista(l2) > prom_conjunto():
        return "La lista N2 es mayor al promedio del conjunto",promedioLista(l2)
    else:
        return "Los dos promedios estan por debajo del promedio conjunto:",prom_conjunto()






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







