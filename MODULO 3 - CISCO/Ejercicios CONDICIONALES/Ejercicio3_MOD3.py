
#Construir un programa el cual solicite el dia de la semana en el que esta y que le imprima el dia de la semana.~

#el condicional if y el elif diran si esta en un dia de la semana o en otra.
semana = input('Escriba que semana es hoy de Lunes a Domingo: ')
if semana == 'Lunes':
    print('El dia de la semana es Lunes')
elif semana == 'Martes':
    print('El dia de la semana es Martes')
elif semana == 'Miercoles':
    print('El dia de la semana es Miercoles')
elif semana == 'Jueves':
    print('El dia de la semana es Jueves')
elif semana == 'Viernes':
    print('El dia de la semana es Viernes')           
elif semana == 'Sabado':
    print('El dia de la semana es Sabado') 
elif semana == 'Domingo':
    print('El dia de la semana es Domingo')        
else:
    print('Esa semana no existe')                     
