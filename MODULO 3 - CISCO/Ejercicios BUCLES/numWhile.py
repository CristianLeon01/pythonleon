
num=1
cont=0
suma = 0
while num!=0:
    num=int(input('ingrese numero'))
    cont=cont+1
    suma = suma + num
print(f'fueron ingresados {cont-1} numeros')
print("La suma de los numeros es: ", suma)

prom = suma / cont-1

print("El promedio de la suma es: ", prom)