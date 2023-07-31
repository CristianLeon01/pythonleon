def VerificacionArchivo(NombreArchivo):
    try:
        archivo = open(NombreArchivo)
        print('El archivo ya existe.')
        lineas = (len(archivo.readlines()))
        print('El archivo tiene', lineas, 'lineas.')
        archivo.close()  
    except FileNotFoundError:
        print('El archivo no existe.')
    except:
        print('Algo salio mal')

NombreArchivo = "C:\\pythonleon\\CISCO\\archivoPrueba.txt"
VerificacionArchivo(NombreArchivo)


