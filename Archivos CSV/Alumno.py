class Alumno:
    def __init__(self,idAlumno,notaUno,notaDos,notaTres):
        self.__idAlumno=idAlumno
        self.__notaUno=notaUno
        self.__notaDos=notaDos
        self.__notaTres=notaTres
    def verDatos(self):
        return f"{self.__idAlumno} {self.__notaUno} {self.__notaDos} {self.__notaTres}"
    def getNotaUno(self):
        return self.__notaUno
    def getNotaDos(self):
        return self.__notaDos
    def getNotaTres(self):
        return self.__notaTres