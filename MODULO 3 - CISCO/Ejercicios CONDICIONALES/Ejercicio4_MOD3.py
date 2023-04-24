
#Construir un programa en el cual se ingrese un numero entero y se diga si es par o impar.

numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(numero, "es un número par.")
else:
    print(numero, "es un número impar.")
