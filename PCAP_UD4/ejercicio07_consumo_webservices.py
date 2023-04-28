#clave = 5f2Oa649 ee6e8770

import requests
import json
key = "5f2Oa649"
titulo = input ("Introduce el título: ")
url = f"http://www.omdbapi.com/?apikey=5f2Oa649&t={titulo}"
resp = requests.get (url)
if resp.status_code==200:
    informacion == json.loads(resp.text)

fichero = open(titulo + ".movie", mode = "wt", encoding= "utf-8")
fichero.write(titulo)
fichero.write("\n")

fichero.write(Titulo, +"\n")
fichero.write(Director, +"\n")
fichero.write(Runtime, +"\n")
fichero.write(Year, +"\n")
fichero.write(Actors, +"\n")

fichero.write("\n")
fichero.close() 


print(informacion["Title"])
print(informacion["Director"])

