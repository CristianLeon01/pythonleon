import mysql.connector

db=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "contratosPSN"
)

class Candidato ():
    def __init__(self, tipoDocumento, numDocumento, nombre, email, telefono):
        self.__tipoDocumento = tipoDocumento
        self.__numDocumento = numDocumento 
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono

    def getTipoDocumento (self):
        return self.__tipoDocumento
    
    def getNumDocumento (self):
        return self.__numDocumento
    
    def getNombre (self):
        return self.__nombre
    
    def getEmail (self):
        return self.__email
    
    def getTelefono (self):
        return self.__telefono
    
    def agregarCandidatos ():
        tipoDocumento = input("Ingrese su tipo de documento:")
        numDocumento = int(input ("Ingrese su numero de documento:"))
        nombre = input("Ingrese su nombre:")
        email = input("Ingrese su correo electronico:")
        telefono = int(input("Ingrese su numero de telefono:"))
        insert = ("insert into candidato (tipoDocumento, numDocumento, nombre, email, telefono) VALUES ('"+tipoDocumento+"', '" +numDocumento+ "', '" +nombre+ "', '"+email+ "', '" +telefono+"')")   
        cursor = db.cursor()
        cursor.execute (insert,cursor)

    agregarCandidatos ()
    
    def getDatos (self):
        return self.__tipoDocumento, self.__numDocumento, self.__nombre, self.__email, self.__telefono