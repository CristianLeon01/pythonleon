l1 = [3, 8, 10, 6, 2]

try:
    indice = int(input("Ingrese el índice que desea buscar en la lista: "))
    x = l1[indice]
    print(f'El elemento en el índice {indice} es {x}')
except IndexError:
    print("El índice ingresado está fuera del rango de la lista.")
except ValueError:
    print("Debe ingresar un número entero como índice.")

#IndexError