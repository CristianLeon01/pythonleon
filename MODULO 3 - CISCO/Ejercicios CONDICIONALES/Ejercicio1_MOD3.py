
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

#se asigna una variable en la cual se guarda la edad
edad = int(input("Digite su edad por favor: "))

#se utiliza el condicional if para establecer una respectiva condicion
if edad>=18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")