
#Construir un programa que al recibir 2 numeros enteros, diga si un numero es divisior de otro.
#INCOMPLETO
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

while num1 % num2 !=0:
    print("Escribalos Nuevamente:")
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))

    if num1 % num2 == 0:
        print( num2, "es divisor de", num1)
    elif num2 % num1 == 0:
        print( num1, "es divisor de", num2)
    






