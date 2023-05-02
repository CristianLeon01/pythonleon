#Solicitar al usuario un número de hasta 9 dígitos e imprimirlo en orden contrario.

num = int(input("Ingresa un número de hasta 9 dígitos: "))

U = num % 10
D = num % 100 // 10
C = num % 1000 // 100
M = num % 10000 // 1000
UM = num % 100000 // 10000
DM = num % 1000000 // 100000
CM = num % 10000000 // 1000000
MM = num % 100000000 // 10000000
DM2 = num // 100000000

print(U, D, C, M, UM, DM, CM, MM, DM2)
