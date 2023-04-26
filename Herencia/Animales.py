from SeresVivos import SerVivo
class Animal:
    def __init__(self, familia, nombre):
        self.familia = familia
        self.nombre = nombre

    def comer(self):
        print("Soy un animal y estoy comiendo...")

    def reproducir(self):
        print("Soy un animal y me estoy reproduciendo...")


class AnimalEstatico(Animal, SerVivo):
    def __int__(self, familia, nombre,  rugosidad):
        super().__init__(familia, nombre)
        self.rugosidad = rugosidad
    def acoplar(self):
        print("Soy un animal y me estoy acoplando...")

    def comer(self):
        print("Soy un AnimalEstatico y estoy comiendo...")

if __name__ == "__main__":
    coral = AnimalEstatico("Molusco", "Coral")
    coral.comer()
    coral.reproducir()
    coral.acoplar()
    coral.decrementar_reisgo()