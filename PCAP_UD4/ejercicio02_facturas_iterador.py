class Factura:
    def __init__(self, nombre, importe) -> None:
        self.nombre = nombre
        self.importe = importe
        self.estado="Pendiente"
    def __repr__(self):
        return(f"{self.nombre}:{self.importe}:{self.estado}")
class Administracion:
    def __init__(self) -> None:
        self.lista_facturas = list()

    def agregar_factura(self, factura : Factura):
        self.lista_facturas.append(factura)
        
    def pagar_factura(self, nombre):
        for f in self.lista_facturas:
            if f.nombre==nombre:
                f.estado="Pagado"
                break
    def __iter__(self):
        self.__facturas_impagadas = [ factura for factura in self.lista_facturas if factura.estado=="Pendiente"]
        self.__indice = -1
        return self
    def __next_(self):
        self.__indice+=1
        if (self.__indice==len(self.__facturas_impagadas)):
            raise StopIteration()
        return self.__facturas_impagadas[self.__indice]

    #VER EL DEL PROFE

adm = Administracion()
f1 = Factura("f1", 1000)
f2 = Factura("f2", 2000)
f3 = Factura("f3", 3000)

adm.agregar_factura(f1)
adm.agregar_factura(f2)
adm.agregar_factura(f3)
adm.pagar_factura(f2)
print(adm.lista_facturas)