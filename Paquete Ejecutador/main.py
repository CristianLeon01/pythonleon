import sys
from sys import path
path.append ("C:\\pythonleon\\PAQUTE_D_y_C\\Listas")

import PAQUTE_D_y_C.Listas
import PAQUTE_D_y_C.Listas.listas

print(PAQUTE_D_y_C.Listas.listas.llenarLista(2,30))

path.append ("C:\\pythonleon\\PAQUTE_D_y_C\\Diccionario")

import PAQUTE_D_y_C.Diccionario
import PAQUTE_D_y_C.Diccionario.diccionario

print(PAQUTE_D_y_C.Diccionario.diccionario.llenar_diccionario())
