#Escribir un programa que visualice la siguiente figura, utilizando ciclos.

num_lin = int(input("Ingresa el número de líneas que quieres imprimir: "))

for i in range(1, num_lin + 1):
    for j in range(i):
        print("*", end=" ")
    print()

#for

