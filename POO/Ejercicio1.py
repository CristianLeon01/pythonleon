class Empleado:
    suma = 0
    contador = 0
    def __init__(self, nombre, cargo, salario):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario
        self.__horaFinal = 0

    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getCargo(self):
        return self.__cargo
    def setCargo(self, cargo):
        self.__cargo = cargo

    def getSalario(self):
        return self.__salario
    def setSalario(self, salario):
        self.__salario = salario

    def calcHora(self):
        porHora = self.__salario // 25
        self.__horaFinal = porHora // 9
        return str(self.__nombre) + " " + "gana " + str(self.__horaFinal) + "$" + " por hora."

    def increICP(self):
        salario = 0
        if self.__salario >= 1160000:
            salario = self.__salario * 0.1312 + self.__salario
        else:
            salario = self.__salario * 0.1612 + self.__salario
        return "El incremento del ICP al salario de "+ str(self.__nombre) + " es de: " + str(salario)
    

    def horasExtras(self, horas_extras):
        if horas_extras <= 2:
            if horas_extras == 1:
                salario_final = self.__salario + (self.__horaFinal * 25)
                return "El salario final de " + str(self.__nombre) + " con las Horas extras es de: " + str(salario_final) + "$"
            elif horas_extras == 2:
                salario_final = self.__salario + (2 * self.__horaFinal * 25)
                return "El salario final de " + str(self.__nombre) + " con las Horas extras es de: " + str(salario_final) + "$"
        else:
            salario_final = "Solo es permitido 1 o 2 horas extras.."
        return salario_final
    
    
    def sumaSalarios(self):
        Empleado.suma = (p1.getSalario() + p2.getSalario() + p3.getSalario())
        return "La suma de todos los salarios es: " + str(Empleado.suma) + "$"
    
    def promSalarios(self):
        Empleado.contador = Empleado.suma // 3
        return "El promedio de los 3 salarios es de : " + str(Empleado.contador) + "$"
        
    def getDatos(self):
        return self.__nombre, self.__cargo, self.__salario


p1 = Empleado('Carlos', 'Administrador', 1130000)
p2 = Empleado('Lucia', 'Secretario', 3530000)
p3 = Empleado('Pedro', 'Director', 12550000)

ob1 = Empleado('','','')

print()
print(p1.getDatos())
print(p2.getDatos())
print(p3.getDatos())
print()
print(p1.calcHora())
print(p2.calcHora())
print(p3.calcHora())
print()
print(p1.increICP())
print(p2.increICP())
print(p3.increICP())
print()
print(p1.horasExtras(3))
print(p2.horasExtras(2))
print(p3.horasExtras(1))
print()
print(ob1.sumaSalarios())
print()
print(ob1.promSalarios())
print()