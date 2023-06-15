from Persona import *
class Instructor(Perosna):
    def __init__(self, id, codigo, nombre, direccion, telefono, profesion, especialidad, cargo, salario):
        super().__init__(id, codigo, nombre, direccion, telefono)
        self.__profesion__=profesion
        self.__especialidad__=especialidad
        self.__cargo__=cargo
        self.__salario__=salario
    def mostrarInfo(self):
        return self.id, self.codigo, self.nombre, self.direccion, self.telefono, self.__profesion__, self.__especialidad__, self.__cargo__,  self.__salario__
    
