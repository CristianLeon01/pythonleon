def agregarDatos(NombreArchivo):
    try:
        with open(NombreArchivo, "w") as archivo:

            Nombre = input("Digite su nombre: ")
            Numero = input("Digite su numero de telefono: ")
            Sexo = input("Digite su tipo de sexo: ")

            archivo.write(f"{Nombre},{Numero},{Sexo}\n")

        print('Datos agregados correctamente al archivo.')

    except Exception:
        print('Algo salio mal:')

NombreArchivo = "C:\\Clon Respositorio\\pythonleon\\CISCO\\datosPersonales01.txt"
agregarDatos(NombreArchivo)