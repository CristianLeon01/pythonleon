#Calcular el máximo de números positivos introducidos por teclado, sabiendo que metemos números hasta que introduzcamos uno negativo. El negativo no cuenta.

num = int(input("Ingresa un número positivo: "))

max = num

while num >= 0:
    num = int(input("Ingresa otro número positivo o uno negativo para salir: "))
    if num > max:
        max = num

print("El número máximo positivo ingresado es:", max)

#WHILE
