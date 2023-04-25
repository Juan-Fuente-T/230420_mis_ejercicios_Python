lista = ["rbol.jpg", "seta.png", "Arbusto.gif"]


#lista_nueva = []
"""lista_nueva = list()#otra opcion para lista
for planta in lista:
    nombre=planta[0:-4]
    lista_nueva.append(nombre)
    print(lista_nueva)
    #Contruccion de una nueva lista con los nombres de los archivos sin extension"""

    
lista_nueva=[planta[0:-4] for planta in lista]
print(lista_nueva)

lista_nueva_mayusculas = [planta.upper() for planta in lista]
print(lista_nueva_mayusculas)

#sustituir letras a por simbolo @
lista_arrobas = [planta.replace ("a","@") for planta in lista]
print(lista_arrobas)