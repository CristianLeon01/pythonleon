import math

def formCuadraticas():
    try:
        a = int(input('Digite un nuemero A: '))
        b = int(input('Digite un nuemero B: '))
        c = int(input('Digite un nuemero C: '))

        x = math.sqrt (b**b - (4 * a * c))
        z = -b - x
        y = 2 * a

        res = z / y
        print(res)
        
    except ValueError:
        print('Valor no admitido')
    except ZeroDivisionError:
        print('No se puede dividir por 0')


formCuadraticas()

# def formCuadraticasSuma():
#     a = int(input('Digite un nuemero A: '))
#     b = int(input('Digite un nuemero B: '))
#     c = int(input('Digite un nuemero C: '))

#     x = math.sqrt (b**b - (4 * a * c))
#     z = -b + x
#     y = 2 * a

#     res = z / y
#     print(res)
    
# formCuadraticasSuma()