#Determinar cuales y cuantos números perfectos hay entre 1 y 1000?

# Verificamos cuáles y cuántos números perfectos hay entre 1 y 1000
for num in range(1, 1001):
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i
            

    if suma_divisores == num:
        print(num, "es un número perfecto")

#for
