
#Escribe un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1
#hasta ese número (incluido).

#se le solicita un numero al usuario
numero = int(input("Ingrese un número entero positivo: "))

#se usa el bucle for para sumarle mas 1 al la variable 
for i in range(1, numero + 1, 2):
    
    #se imprimira solo los numeros impares
    print(i)
