import random

rango = int(input("Ingrese el rango de la lista: "))
tam = int(input("Ingrese el tamaño de la lista: "))

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

l1=llenarLista(tam,rango)

print(l1)

print(sumaLista(l1))

print(promedioLista(l1))
