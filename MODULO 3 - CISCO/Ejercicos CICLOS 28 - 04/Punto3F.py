#Determinar si un número es o no es perfecto.

num = int(input("Ingresa un número: "))

# Inicializamos la suma de los divisores propios en 0
suma_divisores = 0

# Encontramos los divisores propios del número
for i in range(1, num):
    if num % i == 0:
        suma_divisores += i

# Comprobamos si la suma de los divisores propios es igual al número
if suma_divisores == num:
    print(num, "es un número perfecto")
else:
    print(num, "no es un número perfecto")

#for
