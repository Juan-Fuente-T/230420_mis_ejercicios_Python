class Serie: 
    def __init__(self, titulo, sinopsis, numero_temporadas) -> None:
        self.titulo = titulo
        self.sinopsis = sinopsis
        self. numero_temporadas = numero_temporadas

    def guardar (self):
        fichero = open(self.titulo + ".serie", mode = "w", encoding= "utf-8")
        fichero.write(self.titulo)
        fichero.write("\n")
        fichero.write(self.sinopsis +"\n")
        fichero.write(str(self.numero_temporadas))
        fichero.write("\n")
        fichero.close() 

    def autoguardar(self)
        fichero = open(self.titulo + ".serie", mode = "w", encoding= "utf-8")
        for v in self.__init__values
        #SEGUIR VIENDO EL DEL PROFE


lcdlp = Serie("La casa de la pradera", "Episodio 1", 20)
lcdlp.guardar()