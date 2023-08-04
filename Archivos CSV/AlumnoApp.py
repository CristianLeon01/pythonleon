import csv
from Alumno import *

notaUno = []
notaDos = []
notaTres = []

with open('C:\\Clon Respositorio\\pythonleon\\Archivos CSV\\python-csv-main\\notes.csv', encoding='utf-8') as csvDataFile:
    csvReader = csv.reader(csvDataFile)

    for row in csvReader:
        not1 = Alumno(row[0], (row[1]), (row[2]), (row[3]))
        notaUno.append(not1)
        print('ID:', row[0])

print()
print("NOTA DEL PRIMER EXAMEN")
for n1 in notaUno:
    print(n1.getNotaUno())

print()

sumaN1 = 0
for n1 in notaUno:
    nota1 = n1.getNotaUno()
    try:
        sumaN1 += float(nota1)  
    except ValueError:
        pass
print("Suma de las notas del primer examen:", sumaN1)

archivo = 'C:\\Clon Respositorio\\pythonleon\\Archivos CSV\\Archivos TXT\\sumaNotasPrimerExamen.txt'
with open(archivo, 'w') as sN1:
    sN1.write("Suma de las notas del primer examen: " + str(sumaN1))

#-----------------------------//----------------------------------//----------------------------------------------------#

with open('C:\\Clon Respositorio\\pythonleon\\Archivos CSV\\python-csv-main\\notes.csv', encoding='utf-8') as csvDataFile:
    csvReader = csv.reader(csvDataFile)

    for row in csvReader:
        not2 = Alumno(row[0], (row[1]), (row[2]), (row[3]))
        notaDos.append(not2)

print()
print("NOTA DEL SEGUNDO EXAMEN")
for n2 in notaDos:
    print(n2.getNotaDos())

sumaN2 = 0
for n2 in notaUno:
    nota2 = n2.getNotaDos()
    try:
        sumaN2 += float(nota2)  
    except ValueError:
        pass
print("Suma de las notas del segundo examen:", sumaN2)

archivo = 'C:\\Clon Respositorio\\pythonleon\\Archivos CSV\\Archivos TXT\\sumaNotasPrimerExamen.txt'
with open(archivo, 'a') as sN2:
    sN2.write("\nSuma de las notas del segundo examen: " + str(sumaN2))

#-----------------------------//----------------------------------//----------------------------------------------------#

with open('C:\\Clon Respositorio\\pythonleon\\Archivos CSV\\python-csv-main\\notes.csv', encoding='utf-8') as csvDataFile:
    csvReader = csv.reader(csvDataFile)

    for row in csvReader:
        not3 = Alumno(row[0], (row[1]), (row[2]), (row[3]))
        notaTres.append(not3)

print()
print("NOTA DEL TERCER EXAMEN")
for n3 in notaTres:
    print(n3.getNotaTres())

sumaN3 = 0
for n3 in notaUno:
    nota3 = n3.getNotaTres()
    try:
        sumaN3 += float(nota3)  
    except ValueError:
        pass
print("Suma de las notas del tercer examen:", sumaN3)

archivo = 'C:\\Clon Respositorio\\pythonleon\\Archivos CSV\\Archivos TXT\\sumaNotasPrimerExamen.txt'
with open(archivo, 'a') as sN3:
    sN3.write("\nSuma de las notas del segundo examen: " + str(sumaN3))

archivo = 'C:\\Clon Respositorio\\pythonleon\\Archivos CSV\\Archivos TXT\\sumaNotasPrimerExamen.txt'
with open(archivo, 'a') as espacio:
    espacio.write("\n ")

#-----------------------------//----------------------------------//----------------------------------------------------#

proN1=sumaN1/len(notaUno)
print(proN1)

