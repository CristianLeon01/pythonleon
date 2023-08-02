import csv

with open('C:\\Users\\leons\\OneDrive\\Documentos\\Personas.csv') as per:
    reader = csv.reader(per)
    for row in reader:
        print('Nombre: {0}, Edad: {1}, Pais: {2}'.format(row[0], row[1], row[2]))
