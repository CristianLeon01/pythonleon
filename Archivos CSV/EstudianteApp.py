from Estudiante import *
import csv
estudiantes=[]
with open('C:\\pythonleon\\Archivos CSV\\Saber_11__2019-2.csv') as csvDataFile:
    csvReader=csv.reader(csvDataFile)
    for row in csvReader:
        #print(row)
        objeto=Estudiante(row[38],row[1],row[2],row[3])
        #print(objeto.verDatos())
        estudiantes.append(objeto)
        print('Codigo Icfes:',row[38])
        # print('last name:',row[1])
        # print('email:',row[2])
        # print('id:',row[3])
# for es in estudiantes:
#     print(es.getCodIcfes())