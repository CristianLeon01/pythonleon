import random

rango = int(input("Ingrese el rango de la lista: "))
tam = int(input("Ingrese el tamaño de la lista: "))

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

l1=llenarLista(tam,rango)

def list_mediana(lista):
    mediana = 0 
    if tam % 2 == 0:
        num1 = tam // 2
        num2 = num1 -1
        mediana = (lista[num1]+lista[num2]) // 2
    else:
        num_imp = tam // 2
        mediana = (lista[num_imp])
          
    return mediana


def list_moda(lista):
    max = 0
    for num in lista:
        cont = 0
        for x in lista:
            if num == x:
                cont +=1
        if cont > max:
            max = cont
            moda =num

    return moda

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


def orden_ascendente(lista):
    for i in range(tam-1):
        for j in range(i+1,tam):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista


def orden_descendente(lista):
    for i in range(tam-1):
        for j in range(i+1,tam):
            if lista[i]<lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista


print()
print("Lista Original:",l1)

print()
print("Lista de Suma:",sumaLista(l1))
print()

print("Lista Promedio:",promedioLista(l1))
print()

print("Numero Mayor:",numero_mayor(l1))
print("Numero Menor:",numero_menor(l1))
print()

print("Lista en Orden ascendente:",orden_ascendente(l1))
print("Lista en Orden descendente:",orden_descendente(l1))
print()

print("Mediana:",list_mediana(l1))
print("Moda:",list_moda(l1))
print()
#version Funciones y Listas V2