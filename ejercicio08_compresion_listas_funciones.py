def censor(palabra):
    palabras_prohibidas = ("mameluco", "monopatín", "hereje")
    if palabra in palabras_prohibidas:
        return"***"
    return palabra
texto ="El hereje arragó el monopatín y se lo presto al mameluco"
lista_palabras = texto.split()

palabras_finales =  [censor(palabra) for palabra in lista_palabras]
#reconstruimos el str a partir de los elementos de la lista
palabras_finales = " ".join(palabras_finales)
print(palabras_finales)