#Determinar cuales son los múltiplos de 5 comprendidos entre 1 y N.

n = int(input("Ingrese un numero entero porsitivo: "))

for i in range(1, n):
    if i % 5 == 0:
        print(i, "es multiplo de 5")
    print(i)

#for