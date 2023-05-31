def llenar_diccionario():
    diccionario = {} 
    
    while True:
        clave = input("Ingresa una clave (o 'salir' para terminar): ")
        if clave == "salir":
            break
        
        valor = input("Ingresa un valor: ")
        diccionario[clave] = valor
    
    return diccionario


d1 = llenar_diccionario()
print("Diccionario:", d1)