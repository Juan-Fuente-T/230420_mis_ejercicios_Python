fichero = open("datos.txt", mode = "wt", encoding= "utf-8")
fichero.write("Linea 1\n")
fichero.write("Linea 2\n")
fichero.write("Linea 3\n")
fichero.close()

fichero = open("datos.txt", encoding= "utf-8")

datos = fichero.read(4)
datos = fichero.read(3)
datos=fichero.seek(0)

datos = fichero.readline()
datos = fichero.readline()

datos = fichero.readlines()

datos_limpios = map(lambda linea : linea.replace ("\n", " ")) #ver profe

print(datos)
fichero.close()