import random

rango = int(input("Ingrese el rango de la lista: "))
tam = int(input("Ingrese el tamaño de la lista: "))

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

l1=llenarLista(tam,rango)

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum


def promedioLista(lista):
    return sumaLista(lista)/len(lista)


def numero_mayor(lista):
    mayor = 0
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor
        

def numero_menor(lista):
    Menor = 1000000
    for i in lista:
        if i < Menor:
            Menor = i
    return Menor


print(l1)

print(sumaLista(l1))

print(promedioLista(l1))

print(numero_mayor(l1))

print(numero_menor(l1))

#version Funciones y Listas V2