
#Calcular todos los numero de 3 cifras tales que la suma de los cubos de la cifras es igual al valor del numero.

for i in range (100, 500):
    num=i
    u=num%10
    num=num//10
    d=num%10
    c=num//10
    print(c, d, u)
    cubo=(c**3)+(d**3)+(u**3)
    if cubo == i:
        print("ES VALIDO!!!!")
    else:
        print("No es valido")

#for
    