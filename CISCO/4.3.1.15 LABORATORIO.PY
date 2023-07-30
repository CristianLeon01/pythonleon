#Se importar la función 'strerror'
from os import strerror

#Se crear un diccionarioc con claves desde 'a' hasta 'z' e inicializa sus valores en 0
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

#Se crear un diccionario con claves para los signos
signos = {char: 0 for char in "!@#$%^&*()_+-=[]{}|;':,.<>?/`~ "}

#Se solicita al usuario el nombre del archivo a utilizar
file_name = input("Ingresa el nombre del archivo a analizar: ")

try:
    #Se intentar abrir el archivo en modo de lectura 
    file = open(file_name, "rt")

    #Analiza cada linea del archivo
    for line in file:
        #Analiza cada caracter por linea
        for char in line:
            #Condicional que verifica si es una letra
            if char.isalpha():
                #Se convertir el caracter a minúscula y aumentar su contador en el diccionario
                counters[char.lower()] += 1
            else:
                #Se incrementar el contador para los signos
                signos[char] += 1

    # Se cierra el archivo 
    file.close()
    
    #Muestra la repeticion de las letras del archivo
    print("Letras")
    print()
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)

    #Muestra la repeticion de los signos del archivo
    print("Signos")
    print()
    for char, count in signos.items():
        print(char, '->', count)

except IOError as e:
    #Si ocurre un error de E/S durante el manejo del archivo, mostrar el mensaje de error usando 'strerror'
    print("Se produjo un error de E/S: ", strerror(e.errno))

