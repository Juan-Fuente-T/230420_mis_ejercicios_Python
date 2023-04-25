"""Clase CuentaBancaria
Atributos
    Nombre
    Iban
    Saldo(privado)
    gastos_acumulados(privado)
Metodos
    agregar_fondos
    retirar_fondos - Si no hay fondos suficientes lanza una excepcion
    obtener_saldo
    obtener_gastos_acumulados

Nota: Cuando se agregan fondos se introduce un gasto de un euro"""

class CuentaBancaria():
    COMISION_INGRESO = 1#atributo de clase y constante

    def __init__(self, _nombre, _iban, __saldo) -> None: 
        self.nombre = nombre#atributo de clase
        self.iban = iban
        self.__saldo = __saldo
        self.__gastos_acumulados = 0
        
        
    def agregar_fondos(self, cantidad):
        self__saldo+= cantidad - 1 
        self.__gastos_acumulados+=CuentaBancaria.COMISION_INGRESO#atributo de clase

    def retirar_fondos(self, cantidad):
        if cantidad>self.__saldo:
           raise Exception("No hay fondos")
        self.__saldo-= cantidad  

    def obtener_saldo (self):
        return self.__saldo 
           
    def obtener_gastos_acumulados (self):
        return self.__gastos_acumulados
    
    cb1=CuentaBancaria("n1", "iban1", 100)
    cb1.agregar_fondos(10)
    print(c.obtener_saldo())
    print(c.obtener_gastos_acumulados())
    #VER el del profe
    
    


