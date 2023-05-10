#Llenar una lista de n elementos con números generados con la función random. No puede haber números repetidos. Si intenta ingresar a la lista un número que ya existe,
#imprimirlo para anunciar que ese número ya está en el la lista.

import random

lista=[]
tam=random.randint(10,20)

for i in range (tam):
    num=random.randrange(10)
    if num not in lista:  
        lista.append(num)  
    else:
        print(f"El número {num} ya está en la lista.")

print(lista)
print (len(lista)) 
    
