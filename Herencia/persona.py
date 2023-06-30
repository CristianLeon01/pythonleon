from producto import *
from customer import *

class Persona(Cliente):
    def __init__(self,id,tipo,descripcion,nombre,email,telefono,direccion):
        super().__init__(id,tipo,descripcion)
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion= direccion
        self.productos=[]

    def getpersona(self):
        return f"{self.id}, {self.tipo}, {self.descripcion}, {self.nombre}, {self.email}, {self.telefono}, {self.direccion}"

    def agreproductos(self,producto):
        self.productos.append(producto)

    def getlistProductos(self):
        return self.productos

