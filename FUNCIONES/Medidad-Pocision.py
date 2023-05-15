import random

def llenarLista(tam=(200, 2500), rango=(100, 500)):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

l1 = llenarLista()
print(l1)