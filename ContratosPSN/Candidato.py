import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="contratosPSN"
)

class Candidato():
    def __init__(self, tipoDocumento, numDocumento, nombre, email, telefono):
        self.__tipoDocumento = tipoDocumento
        self.__numDocumento = numDocumento
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono

    def getTipoDocumento(self):
        return self.__tipoDocumento

    def getNumDocumento(self):
        return self.__numDocumento

    def getNombre(self):
        return self.__nombre

    def getEmail(self):
        return self.__email

    def getTelefono(self):
        return self.__telefono

    def agregarCandidato():
        tipoDocumento = input("Ingrese su tipo de documento:")
        numDocumento = int(input("Ingrese su numero de documento:"))
        nombre = input("Ingrese su nombre:")
        email = input("Ingrese su correo electronico:")
        telefono = (input("Ingrese su numero de telefono:"))

        insertar = "INSERT INTO candidato (tipoDocumento, numDocumento, nombre, email, telefono) VALUES (%s, %s, %s, %s, %s)"
        valores = (tipoDocumento, numDocumento, nombre, email, telefono)

        cursor = db.cursor()
        cursor.execute(insertar, valores)
        db.commit()
        cursor.close()

    def getDatos(self):
        return self.getTipoDocumento(), self.getNumDocumento(), self.getNombre(), self.getEmail(), self.getTelefono()


Candidato.agregarCandidato()
