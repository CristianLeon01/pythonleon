# Se asigna el valor 100 a la variable x y se imprime su tipo
x=100
print(type(x))

# Se asigna el valor 'Soacha' a la variable x y se imprime su tipo
x='Soacha'
print(type(x))

# Se declara una lista con diferentes tipos de elementos y se imprimen algunos de ellos
lista=['python',100,[1,2,3,[]],'a']
print(type(lista))
print(len(lista))
print(lista[0])
print(lista[1])
print(lista[3])
print(lista[-4])

# Se elimina el segundo último elemento de la lista y se imprime el resultado
del lista[-2]
print(lista)

"""
# Se comenta un bloque de código que genera un error por falta de definición
cuenta1=cuenta()
cuenta2=cuenta()
cuenta3=cuenta()
cuenta1.deposit()
print(type(cuenta1))
cuenta2.deposit()
cuenta3.deposit()
"""
