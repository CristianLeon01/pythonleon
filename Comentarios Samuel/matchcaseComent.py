# Asignamos valores a las variables num1 y num2
num1, num2 = 100, 50

# Imprimimos las opciones del menú
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
print('5-residuo')

# Pedimos al usuario que seleccione una opción
op = int(input('que operacion? '))

# Utilizamos la sintaxis "match" para evaluar la opción seleccionada por el usuario
match op:
    case 1:
        # Si el usuario seleccionó 1, imprimimos la suma de num1 y num2
        print(num1 + num2)
    case 2:
        # Si el usuario seleccionó 2, imprimimos la resta de num1 y num2
        print(num1 - num2)
    case 3:
        # Si el usuario seleccionó 3, imprimimos el producto de num1 y num2
        print(num1 * num2)
    case 4:
        # Si el usuario seleccionó 4, imprimimos el cociente de num1 y num2
        print(num1 / num2)
    case 5:
        # Si el usuario seleccionó 5, imprimimos el residuo de num1 y num2
        print(num1 % num2)
