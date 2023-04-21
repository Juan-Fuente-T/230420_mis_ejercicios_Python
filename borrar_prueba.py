
'''Ejercicio:
Crear una función que reciba un nombre de fichero (la ruta completa)
y devuelva un str con el contenido.'''
contenido_fichero = input ("Introduce la ruta del fichero: ")

def get_fichero(contenido:str):
    fichero = open(contenido_fichero, encoding="utf-8", mode="r")
    info = fichero.read()
    fichero.close()
    return info
    
contenidos = get_fichero(contenido_fichero)
print (contenidos)

'''Crear una función que reciba un str y cambie las letras a por @'''


'''Crear una función que reciba un str y un nombre de fichero (la ruta completa)
y almacene el str en el fichero.'''


"""def escribir_fichero(string:str, ruta_archivo):
    fichero = open(ruta_archivo, encoding="utf-8", mode="w")
    info = fichero.write(string)
    fichero.close()
    return info

string = input ("Introduce un texto: " )
ruta_archivo = input ("¿Donde quieres guardarlo?: ")

escribir_fichero (string, ruta_archivo)"""