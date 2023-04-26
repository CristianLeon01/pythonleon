#Crear un sistema que le solicite 3 numeros al usuario y le imprima cual de esos 3 numero es mayor.

# Pedimos al usuario que ingrese tres números.

x = int(input('ingrese numero: '))
y = int(input('ingrese numero: '))
z = int(input('ingrese numero: '))

# utilizamos condicionales "if" y "else" para identificar el numero mayor.
if x > y:
    if x > z:
        # Si x es mayor que y y z, imprimimos que x es el número mayor
        print(f'el mayor es {x}')
    else:
        # Si x no es mayor que z, significa que z es el número mayor
        print(f'el mayor es {z}')
else:
    if y > z:
        # Si y es mayor que z, imprimimos que y es el número mayor
        print(f'el mayor es {y}')
    else:
        # Si y no es mayor que z, significa que z es el número mayor
        print(f'el mayor es {z}')
