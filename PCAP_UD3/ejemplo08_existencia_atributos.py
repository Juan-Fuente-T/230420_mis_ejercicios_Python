class Serie:
    def __init__(self, titulo, numero_temporadas) -> None:
        self.titulo = titulo
        self.numero_temporadas = numero_temporadas
lou =Serie("The last of us", 1)
    print(lou.titulo)

try:
    print(lou.director)
except AttributeError:
    print("El atributo no existe")

if hasattr(lou, "director"):
    print(lou.director)
else:
    print("El atributo no existe")

    #Ver el del profe