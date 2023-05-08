#Llenar una lista con la serie de Fibonacci, con la cantidad de dígitos que el usuario indique al inicio del programa.

lista_fibonacci = []

num_inicial = int(input("Digite un numero inicial: "))
num_final = int(input("Digite un numero final: "))

for i in range(num_inicial, num_final):
    if i == num_inicial or i == num_inicial+1:
        lista_fibonacci.append(i)
    else:
        lista_fibonacci.append(lista_fibonacci[-1] + lista_fibonacci[-2])
print(lista_fibonacci)
