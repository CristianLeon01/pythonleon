# Inicializamos las variables para la suma, el número mayor y el número menor
suma = 0
numeros = []
mayor = None
menor = None
contador = 0

# Pedimos al usuario que ingrese los números
while True:
    num = int(input("Ingresa un número (0 para salir): "))
    if num == 0:
        break
    suma += num
    contador += 1
    if mayor is None or num > mayor:
        mayor = num
    if menor is None or num < menor:
        menor = num
    numeros = numeros + [num]

# Imprimimos los resultados
print(f"La cantidad de números ingresados es: {contador}")
print(f"La suma de los números ingresados es: {suma}")
if contador > 0:
    print(f"El promedio de los números ingresados es: {suma/contador}")
else:
    print("No se ingresaron números.")
if mayor is not None:
    print(f"El número mayor ingresado es: {mayor}")
if menor is not None:
    print(f"El número menor ingresado es: {menor}")