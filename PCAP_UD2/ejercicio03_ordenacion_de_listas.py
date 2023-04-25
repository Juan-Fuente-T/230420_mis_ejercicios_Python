"""
lista_numeros = [3, 8, 1, 0, 10, 15]
lista_ordenada = sorted(lista_numeros)
print ("Lista original:", lista_numeros)
print("Lista ordenada:", lista_ordenada)
lista_ordenada= sorted(lista_numeros, reverse=True)
print("Lista ordernada al revés: ", lista_ordenada)

lista_ciudades= [
    ("Santiago", 100_000, 9),
    ("Vigo", 200_000, 7),
    ("Pontevedra", 80_000, 9),
    ("Coruña", 150_000, 8),
]

lista_ordenada_ciudades= sorted(lista_ciudades)
print(lista_ordenada_ciudades)

def cuantificar(ciudad):
    return ciudad[2]
lista_ordenada_ciudades=sorted(lista_ciudades, key=cuantificar, reverse=True)
print(lista_ordenada_ciudades)"""

lista_numeros = [3, 8, 1, 0, 10, 15]
lista_numeros.sort(reverse=True)
print(lista_numeros)

lista_ciudades= [
    ("Santiago", 100_000, 9),
    ("Vigo", 200_000, 7),
    ("Pontevedra", 80_000, 9),
    ("Coruña", 150_000, 8),
]
def cuantificar(ciudad):
    return ciudad[2]
lista_ciudades.sort (key=cuantificar, reverse=True)
print (lista_ciudades)

