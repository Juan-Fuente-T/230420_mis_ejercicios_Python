def dividir(d1,d2):
    lista =[0,1,2]
    lista [4] #index error si el indice no existe
    diccionario ={0:"Cero", 1:"Uno"}
    return d1/d2 #ZeroDivisionError si d2==0

try:
    resultado = dividir(5,0)
    print(resultado)
except:
    print("Error")  

try:
    resultado = dividir(5,2)
    print(resultado)
except ZeroDivisionError:
    print("Error: división entre 0")  
except IndexError:
    print("Error:indice inexistente")
except:
    print("Error:No sé que, pero pasa algo")

try:
    resultado = dividir(5,0)
    print(resultado)
except ZeroDivisionError as pelota:
    print(pelota)

