class Persona:
    def __init__(self, _nombre, _color_pelo, _altura) -> None: 
        self.nombre = _nombre
        self.color_pelo = _color_pelo
        self.altura = _altura
        self.vivo = True
def saludar(self):
    print(f"Hola ¿qué tal, {self.nombre}?")

def presentar(self, nombre):
    print(f"Hola {nombre}, soy {self.nombre}?")

persona1 = Persona("Chus", "marrón", 170)#instanciar
persona1.saludar()#invocar a un metodo
persona1.presentar(Lucas)