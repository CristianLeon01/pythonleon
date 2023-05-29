d1 = {
    "perro": "dog",
    "gato": "cat",
    "pájaro": "bird",
    "ratón": "mouse"}

def tuplaAnimales(d1):
    listaEspañol = []
    listaIngles = []
    for clave, valor in d1.items():
        listaEspañol.append(clave)
        listaIngles.append(valor)
    tuplaEspañol = tuple(listaEspañol)
    tuplaIngles = tuple(listaIngles)
    return (tuplaEspañol, tuplaIngles)

tuplaEs, tuplaIn = tuplaAnimales(d1)
print("La tupla en español es:", tuplaEs)
print("La tupla en inglés es:",tuplaIn)
