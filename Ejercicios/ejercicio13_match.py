"""nombre= "Fe"
match nombre:
    case"Ab":
        print("Ab")
    case "Fe":
        print ("Fe")
    case _: 
        print("No se")
..."""
from gtts import gTTS
import os

def leer_receta(nombre_receta):
    nombre_fichero = "./recetas/" + nombre_receta + ".txt"
    fichero = open (nombre_fichero, encoding="utf-8", mode ="r")
    info = fichero.read()
    fichero.close()
    return info
def hacer_locucion(texto):
    audio = gTTS (text=texto, lang="es", slow=False)
    audio.save("locucion.mp3")
    os.system("start locucion.mp3")


    

receta= (input ("Nombre de receta: ")).lower()
match receta:
    case"paella":
        hacer_locucion(leer_receta(receta))
    case "estofado":
        hacer_locucion(leer_receta(receta))
    case _:
        hacer_locucion("No tenemos esa receta")