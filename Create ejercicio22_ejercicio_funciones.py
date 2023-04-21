"""contenido_fichero = input ("Introduce la ruta del fichero: ")

def get_fichero(contenido:str):
    fichero = open(contenido_fichero, encoding="utf-8", mode="r")
    info = fichero.read()
    fichero.close()
    return info
    
contenidos = get_fichero(contenido_fichero)
print (contenidos)"""
    
    #Crear una función que reciba un nombre de fichero (la ruta completa)
#y devuelva un str con el contenido.

#Crear una función que reciba un str y un nombre de fichero (la ruta completa)
#y .almacene el str en el fichero.

def escribir_fichero(texto:str, nombre_fichero):
    contenido_fichero = input ("Introduce un texto: "," y un nombre de fichero" )
    fichero = open(contenido_fichero, encoding="utf-8", mode="w")
    info = fichero.write(texto)
    fichero.close()
    return info
    
contenidos = get_fichero(fichero)
print (contenidos)

def escribir_archivo(ruta, contenido):
    archivo = open(ruta, "w")
    archivo.write(contenido)
    archivo.close()

FORGA
contenido_fichero = input ("Introduce un texto: "," y un nombre de fichero" )

def escribir_fichero(texto:str, nombre_fichero):
    fichero = open(nombre_fichero, encoding="utf-8", mode="w")
    info = fichero.write(texto)
    fichero.close()
    return info
    
contenido = escribir_fichero("iuhihh",C:\Users\Juan\Desktop\proba.txt)
print (contenido)
def sumar(sumando1, sumando2):
    print(sumando1 + sumando2)

sumar(3,4)






