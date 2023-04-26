
# Asignamos las variables "i" y "sum"
i = 1
sum = 0

# Utilizamos un bucle "while" para repetir el código dentro del bucle mientras la condición "i<=5" sea verdadera
while i <= 5:
    # Imprimimos el valor actual de la variable "i"
    print(i)
    
    # Agregamos el valor actual de la variable "i" a la variable "sum"
    sum = sum + i
    
    # Incrementamos la variable "i" en 1
    i += 1 

# Imprimimos la suma total de los números del 1 al 5
print(f'la suma es = {sum}')
