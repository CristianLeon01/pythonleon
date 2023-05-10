import random
import math

lista = [round(random.random()*5,2) for i in range(20,30) ]
print(lista)

lista_completa=['Aprobados' if i > 3 else 'Suspendidos' for i in lista]
lista_Apro=['Aprobados' for i in lista if i > 3 ]
lista_Suspen=['Suspendido' for i in lista if i < 3 ]
print()

print(lista_completa)
print()
print(lista_Apro)
print()
print(lista_Suspen)
print()

lista.sort()
print(lista)
print()

lista_0_1 = [x for x in lista if x < 2]
print("Lista de Cero a Uno", lista_0_1)

print()

lista_2_3 = [x for x in lista if x > 2 and x < 4]
print("Lista de Dos a Tres", lista_2_3)

print()

lista_4_5 = [x for x in lista if x > 4]
print("Lista de Cuatro a Cinco", lista_4_5)

lista_pro = [lista_Apro / len(lista_Apro)]
print()
print(lista_pro)





