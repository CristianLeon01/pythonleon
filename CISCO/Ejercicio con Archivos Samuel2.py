def agregarDatos(NombreArchivo):
    try:
        archivo = open(NombreArchivo)
        Nombre=print(input("Digite su nombre"))
        Numero=print(input("Digite su numero de telefono"))
        Sexo=print(input("Digite su tipo de sexo"))
        datos = (Nombre, Numero, Sexo)
        NombreArchivo.append(datos)
        archivo.close() 

    except FileNotFoundError:
        print('El archivo no existe.')
    except:
        print('Algo salio mal')

NombreArchivo = "C:\\pythonleon\\CISCO\\datosPersonales.txt"
agregarDatos(NombreArchivo)