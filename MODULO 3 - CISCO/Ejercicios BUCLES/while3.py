
#lea dos números garantice que hay uno mayor que el otro si no es el caso pida los de nuevo, reste el menor del mayor y diga cuánto sobra.

# Solicitar al usuario que ingrese dos números enteros
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

# Verificar si los números ingresados son iguales y en caso afirmativo pedir que se ingresen de nuevo.
while num1 == num2:
    print("digite de nuevo los nuemeros")
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

# Comparar los números ingresados y determinar cuál es el mayor.
if num1 > num2:
        print(num1, "es el numero mayor")
        # Calcular la resta del número menor al mayor.
        resta = num1 - num2
        print("la resta del menor al mayor es de: ", resta)

                

elif num2 > num1:
        print(num2, "es el numero mayor")
        # Calcular la resta del número menor al mayor.
        resta = num2 - num1
        print("la resta del menor al mayor es de: ", resta)

while resta !=0:
        print("El resultado se puede seguir restando")
        num_resta = int(input("Digite un numero: "))
        resta = resta - num_resta
        print("La resta es: ", resta)
         
else:
        print("fin")
               
               
