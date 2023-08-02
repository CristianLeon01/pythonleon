def contarCaracteres(NombreArchivo):
    try:
        with open(NombreArchivo, "r") as archivo:
            contenido = archivo.read()
            numCaracteres = len(contenido)

        return numCaracteres

    except FileNotFoundError:
        print('El archivo no existe.')
        return None
    except Exception:
        print('Algo salio mal.')
        return None
    
NombreArchivo = "C:\\Clon Respositorio\\pythonleon\\CISCO\\datosPersonales01.txt"
numCaracteres = contarCaracteres(NombreArchivo)
print(f"El archivo contiene {numCaracteres} caracteres.")

