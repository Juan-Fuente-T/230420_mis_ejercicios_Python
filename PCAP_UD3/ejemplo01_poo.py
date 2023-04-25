class Enemigo:
    #constructor
    def __init__(self, _nombre, _salud, _fuerza) -> None: 
        self.nombre = _nombre
        self.salud = _salud
        self.fuerza = _fuerza
    def __morir(self):
        print("Agghhhh...me muero mucho")
    def recibir_golpe(self, fuerza_golpe):
        print(f"he recibido un golpe de fuerza {fuerza_golpe}")
        self.salud -= fuerza_golpe
        print(f"Mi salud es de {self.salud}")
        if (self.salud<=0):
            self.__morir()

x  = Enemigo("Piolin", 100, 1)#instanciar
x.recibir_golpe(50)
x.recibir_golpe(30)
x.recibir_golpe(30)



"""
Enemigo

#estado-atributos
nombre : str
salud : int
fuerza : int

#compòrtamiento-metodos
atacar(destinatario)
recibir_leñazos(fuerza_leñazo)
morir()"""