import random

tam = random.randint(5,10)

lista = [random.randrange(100)for i in range(tam)]
lista2 = [i//2 for i in lista]

print(lista)
print(lista2)

#copiar el repo del profe