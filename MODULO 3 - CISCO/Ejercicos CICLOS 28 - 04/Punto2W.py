#Determinar si un numero es o no es primo

num = int(input("Ingresa un número: "))

# 0 y 1 no son números primos
if num <= 1:
    print(num, "no es un número primo")
else:
    # Verificamos si el número es divisible por algún número menor que él mismo
    i = 2
    while i < num:
        if num % i == 0:
            print(num, "no es un número primo")
            break
        i += 1
    else:
        print(num, "es un número primo")

#WHILE

