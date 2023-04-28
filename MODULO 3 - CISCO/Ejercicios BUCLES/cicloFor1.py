
#solicité al usuario inicio, fin y cantidad a incrementar o decrementar según el caso. 
#solicitar un número positivo al usuario. diga cuántos múltiplos de n hay en la serie desde cero hasta el número integrado.

incio = int(input("Ingrese el numero de partida: "))
fin = int(input("Ingrese el numero de finalizacion: "))
increment = int(input("Ingrese la cantidad a incrementar o decrementar: "))

n = int(input("ingrese un numero entero postivo: "))

for i in range (incio, fin, increment):
    if i%n==0:
        print(i, "es multiplo de", n)
    else:
        print(i)
    