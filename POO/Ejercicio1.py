class Empleado:
    suma=0
    contador=0
    def __init__(self, nombre, cargo, salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario

    def getNombre(self):
        return self.__nombre  
    def setNombre(self, nombre):
        self.__nombre=nombre

    def getCargo(self):
        return self.__cargo
    def setCargo(self, cargo):
        self.__cargo=cargo

    def getSalario(self):
        return self.__salario
    def setSalario(self, salario):
        self.__salario=salario

    def calcHora(self):
        self.__salario 

    def getDatos(self):
        return self.__nombre, self.__cargo, self.__salario

p1=Empleado('Carlos', 'Administrador', )
p2=Empleado('Lucia', 'Secretario', 1600000)
p3=Empleado('Pedro', 'Director', 4500)
print(p1.getDatos())
print(p2.getDatos())
print(p3.getDatos())

