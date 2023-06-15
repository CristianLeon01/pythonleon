class Perosna:
    def __init__(self, id, codigo, nombre, direccion, telefono):
        self.id=id
        self.codigo=codigo
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
    def mostrarInfo(self):
        return self.id, self.codigo, self.nombre, self.direccion, self.telefono
    

