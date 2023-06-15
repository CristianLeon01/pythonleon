from Persona import *
from Instructor import *
from Coordinador import *

p1 = Perosna (102336322, 1, 'Martin', 'Cra 1 #21-32', 3007722066)
p2 = Perosna (102333478, 2, 'Elias', 'Cra 2 34-32', 3123971034)
p3 = Perosna (112345689, 3, 'Monica', 'Cra 4 #45-78', 3102833961)
print(p1.mostrarInfo())
print()
in1= Instructor (1,101,"Pedro","Cra1 #32-29",3007722066,"Doctor","Terapeuta","Gerente",12000000)
print(in1.mostrarInfo())
print()
coor1 = Coordinador (1,111,"David", "Cra1 #32-33", 3007722066, "01/02/2023", "A102", "Coordinador Academico")
coor2 = Coordinador (1,122,"Milena", "Cra3 #45-56", 3123971034, "01/04/2023", "B101", "Coordinador Administrativo")
coor3 = Coordinador (1,133,"Oscar", "Cra2 #35-12", 3234568122, "01/07/2023", "C100", "Coordinador Programas Rurales")
coor4 = Coordinador (1,144,"Monica", "Cra4 #12-34", 3012457865, "01/02/2023", "A112", "Coordinador Academico")
coor5 = Coordinador (1,155,"Lisa", "Cra7 #23-33", 31230956432, "01/06/2023", "C201", "Coordinador De formacion Profesional")

print(coor1.mostrarInfo())
print(coor2.mostrarInfo())
print(coor3.mostrarInfo())
print(coor4.mostrarInfo())
print(coor5.mostrarInfo())