class Estudiante:
    def __init__(self,codIcfes,codDane,puntEspañol,puntMatematicas):
        self.__codIcfes=codIcfes
        self.__codDane=codDane
        self.__puntEspañol=puntEspañol
        self.__puntMatematicas=puntMatematicas
    def verDatos(self):
        return f"{self.__codIcfes} {self.__codDane} {self.__puntEspañol} {self.__puntMatematicas}"
    def getCodIcfes(self):
        return self.__codIcfes