#Crear un sistema que le solicite 3 numeros al usuario y le imprima cual de esos 3 numero es mayor

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
num3 = int(input("ingrese el tercer numero: "))

if num1>num2:
    if num1>num3:
        print("El numero mayor es: ", num1) 
    else:
        print("El numero mayor es:", num3)

elif num2>num3:
    print("El numero mayor es: ", num2)

else:
    print("El numero mayor es:", num3)