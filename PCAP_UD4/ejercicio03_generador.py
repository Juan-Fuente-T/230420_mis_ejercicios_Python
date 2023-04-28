def get_datos():
    datos =[1,2,3,4,5,6,7,8,9,10]
    return datos

def get_datos_generador():
    datos =[1,2,3,4,5,6,7,8,9,10]
    for dato in datos:
         print("Antes del yield")
         yield dato

if __name__ == "__main__":
    for dato in get_datos_generador():
         print(dato, end="-")