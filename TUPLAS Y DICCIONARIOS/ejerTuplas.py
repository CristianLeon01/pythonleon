import random


tam=random.randint(5,15)
tupla = ()

for i in range (tam):
    num = random.randrange(100) 
    tupla+=(num,)

print(tupla)

tupla2=(tupla[:5])

print(tupla2)

tupla3=(tupla[5:])

print(tupla3)