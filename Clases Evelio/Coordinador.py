from Persona import *
class Coordinador(Perosna):
    def __init__(self, id, codigo, nombre, direccion, telefono, fecha_ingreso, dir_oficina, nombre_coordinacion):
        super().__init__(id, codigo, nombre, direccion, telefono)
        self._fecha_ingreso=fecha_ingreso
        self._dir_oficina=dir_oficina
        self._nombre_coordinacion=nombre_coordinacion

    def mostrarInfo(self):
        return self.id, self.codigo, self.nombre, self.direccion, self.telefono, self._fecha_ingreso, self._dir_oficina, self._nombre_coordinacion
    #     self._persona1=[]
    #     self._persona2=[]
    #     self._persona3=[]

    # def agreP1(self) 
    