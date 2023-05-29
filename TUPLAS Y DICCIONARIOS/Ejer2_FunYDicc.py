print()
print()

d1 = {
    "perro": "dog",
    "gato": "cat",
    "pájaro": "bird",
    "ratón": "mouse"}

d2 = {
    "dog": "perro",
    "cat": "gato",
    "bird": "pájaro",
    "mouse": "ratón"}

print("Este es el diccionario de español a inglés:", d1)
print()
print("Este es el diccionario de inglés a español:", d2)

def agregarEsIn1(d1):
    d1["cocodrilo"] = "crocodile"
    d1["pato"] = "duck"
    return d1

def agregarEsIn2(d1):
    d1["tucán"] = "toucan"
    d1["gallina"] = "hen"
    return d1

def agregarInEs3(d2):
    d2["pig"] = "cerdo"
    d2["bear"] = "oso"
    return d2

def agregarInEs4(d2):
    d2["rhinoceros"] = "rinoceronte"
    d2["horse"] = "caballo"
    return d2

print()

while True:
    print('1- Actualización 1 del primer diccionario')
    print('2- Actualización 2 del primer diccionario')
    print('3- Actualización 1 del segundo diccionario')
    print('4- Actualización 2 del segundo diccionario')
    print()
    opcion = input("¿Qué actualización desea realizar? (1/2/3/4): ")

    if opcion == "1":        
        print("La actualización 1 del primer diccionario es:", agregarEsIn1(d1))
    elif opcion == "2":       
        print("La actualización 2 del primer diccionario es:", agregarEsIn2(d1))
    elif opcion == "3":
        print("La actualización 1 del segundo diccionario es:", agregarInEs3(d2))
    elif opcion == "4":
        print("La actualización 2 del segundo diccionario es:", agregarInEs4(d2))
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

