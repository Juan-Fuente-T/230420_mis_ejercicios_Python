def convertir(fruta : object) -> object:
    fruta.cambiar_nombre(nuevo_nombre)
class Fruta:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    def cambiar_nombre(self, nombre):
        self.nombre = nombre

pera = Fruta("Pera")
convertir(pera, "Manzana")
print(pera.nombre)