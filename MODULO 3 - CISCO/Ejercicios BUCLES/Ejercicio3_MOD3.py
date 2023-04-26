
#Crea un algoritmo para la sucesión de Fibonacci.

# se define la cantidad de números de la serie a calcular
n = 10

# iniciar con los primeros dos números de la serie
a, b = 0, 1

# Imprimir los primeros dos números de la serie
print(a)
print(b)

# Calcular los siguientes n-2 números de la serie y mostrarlos en pantalla
for i in range(1, n-1):
    c = a + b
    print(c)
    a, b = b, c

