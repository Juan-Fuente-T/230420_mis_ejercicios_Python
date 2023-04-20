capitales = ["A Coruña", "Lugo","Orense", "Pontevedra"]
poblaciones = [246000, 97000, 104000, 82000]

informacion =zip(capitales, poblaciones)
"""for capital, poblacion in informacion:
    print(capital, informacion)"""
"""lista_ciudades = list(informacion)
print(lista_ciudades)"""

capitales = ["A Coruña", "Lugo","Orense", "Pontevedra", "Santiago"]
poblaciones = [246000, 97000, 104000, 82000]
informacion =zip(capitales, poblaciones, strict=True)#provocará error si las listas tienen tamaños distintos
lista_ciudades = list(informacion)