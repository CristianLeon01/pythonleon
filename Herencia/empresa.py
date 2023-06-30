from customer import *
class Empresa(Cliente):
    def __init__(self,id,tipo,descripcion,nombre,telefono,email):
        super().__init__(id, tipo, descripcion)
        self.nombre = nombre
        self.telefono = telefono
        self.email = email