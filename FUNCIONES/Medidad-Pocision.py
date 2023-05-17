import random

def llenar_lista(tam_i, tam_f, rango_i, rango_f):
    lista = [random.randint(rango_i, rango_f) for _ in range(tam_i, tam_f)]
    return lista

listaGeneral = llenar_lista(50, 90, 100, 500)
print(listaGeneral)

def ascendente(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

print(ascendente(listaGeneral))


def cuartil(lista):
    n = len(lista)
    listaCuartil = []
    for i in range(1, 4):
        if n % 2 != 0:
            formula = (i * (n + 1)) / 4
            posicion = lista[int(formula) - 1]
        else:
            formula = (i * n) / 4
            posicion1 = lista[int(formula) - 1]
            posicion2 = lista[int(formula)]
            posicion = (posicion1 + posicion2) / 2
        print(f"Q{i} = {posicion}")
        listaCuartil.append(posicion)
    return listaCuartil

print(cuartil(listaGeneral))


def quintil(lista):
    n = len(lista)
    listaQuintil = []
    for k in range(1, 5):
        if n % 2 != 0:
            formula = (k * (n + 1)) / 5
            posicion = lista[int(formula) - 1]
        else:
            formula = (k * n) / 5
            posicion1 = lista[int((k * n) / 5) - 1]
            posicion2 = lista[int((k * n) / 5)]
            posicion = (posicion1 + posicion2) / 2
        print(f"Q{k} = {posicion}")
        listaQuintil.append(posicion)
    return listaQuintil

print(quintil(listaGeneral))


