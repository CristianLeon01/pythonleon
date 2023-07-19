try:
    my_dict = {"a": 1, "b": 2, "c": 3}
    key = input("Ingrese una clave para obtener el valor del diccionario: ")
    value = my_dict[key]
    print(f"El valor asociado a la clave '{key}' es: {value}")
except KeyError:
    print("La clave ingresada no se encuentra en el diccionario.")

#KeyError