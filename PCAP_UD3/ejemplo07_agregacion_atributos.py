class Vehiculo:
    activo = True
    def __init__(self) -> None:
        self.marca = "marca"
        self.modelo = "modelo"

    def arrancar(self):
        pass

v1 = Vehiculo()
v2 = Vehiculo ()
print(dir(v1))
