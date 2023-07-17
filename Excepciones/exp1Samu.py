x = int(input('Ingrese un numero: '))
while x < 10:
    print('Digite nuevamente el numero')
    x = int(input('Ingrese un numero: '))

op = x / 0
print(op)

#------------------------------------------

try:
    x = int(input('Ingrese un numero: '))
    while x < 10:
        print('Digite nuevamente el numero')
        x = int(input('Ingrese un numero: '))
    op = x / 4
    print(op)
except ValueError:
    print("Valor no admitido")
except ZeroDivisionError:
    print("No se puede dividir por cero")


#------------------------------------------


try:
    x = int(input('Ingrese un numero: '))
    while x < 10:
        print('Digite nuevamente el numero')
        x = int(input('Ingrese un numero: '))
    op = x / 0
    print(op)
except ValueError:
    print("Valor no admitido")
except ZeroDivisionError:
    print("No se puede dividir por cero")    