def saludar ():
    print("Ola")
saludar()

def saludar_con_nombre (nombre:str):
    print("Ola", nombre)
saludar_con_nombre ("Javier")


def get_saludo (nombre:str) -> str:
    return f"Ola {nombre}"
print (get_saludo("Javier"))

def sumar (sumando1, sumando2):
    print (sumando1+sumando2)

sumar (3,4)


def get_suma(sumando1, sumando2=0):
    return sumando1+sumando2
print((5,))
print((5,3))

def funcion_opcional(par1,par2=0,par3=0,par4=0):
    print(par1,par2,par3,par4)
funcion_opcional(3)
funcion_opcional(5,1)
funcion_opcional(5,5,5,5)
funcion_opcional(2,par3=8)

def funcion_indeterminada(*args):
    print(type(args))
    for arg in args:
        print(arg,end="-")

    
funcion_indeterminada(3)
funcion_indeterminada(3,8)
funcion_indeterminada(3,6,"Hola")
funcion_indeterminada(3,8,True,3.5,"Ola",7)

def funcion_diccionario(**kvargs):
    for k,v in kvargs.items()
    print(k,v)

funcion_diccionario(nombre="David", altura=180, activo = True)