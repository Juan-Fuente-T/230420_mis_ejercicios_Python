cadena = "Me gusta tomar el sol en invierno"
busqueda = input("Introduce texto a buscar: ")

try: 
    posicion = cadena.index(busqueda)
    parte_izquierda = cadena[:posicion]
    parte_derecha = cadena[posicion:]
    print (parte_izquierda)
    print (parte_derecha)
    print(posicion)
except ValueError:
    print (f"No encuentro '{busqueda}' dentro de '{cadena}'")
