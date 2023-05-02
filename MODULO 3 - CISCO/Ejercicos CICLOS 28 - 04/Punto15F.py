# Diseñar e implementar un programa que solicite a su usuario un valor no negativo n y visualice la siguiente salida:
# 1 2 3
# 1 2
# 1

a=int(input("Ingrese un valor no negativo: "))
for i in range(a, 0, -1):
    for j in range(1, i+1):
        print(j, end='')
    print()

#for