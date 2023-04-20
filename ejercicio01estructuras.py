#Listas
lista = [3, 8, 10, "Automovil"]
#Acceso a un elemento
print (lista[0]) 
#Recorrer todos los elementos
for elemento in lista:
    print (elemento)

#Tupla
tupla = (3, 8, 10, "Automovil")
tupla = (3,)
#Acceso a un elemento
print(tupla[0]) #Mostrar el primer elemento de la tupla
#Recorrer todos los elementos
for elemento in tupla:
    print(elemento)


#Set(conjunto)
conjunto = {3, 8, 10, "Automovil"}
#Recorrer todos los elementos   
for elemento in conjunto:
    print(elemento)

#Dict (diccionario)
diccionario = {3:"Tres", "Ocho":8, "Diez":10, "Objeto":"Automovil"}
#Acceso a un elemento
print (diccionario["Ocho"])
#Recorrer todos los elementos
#Recorrer todos las claves
for clave in diccionario.keys():
    print(clave)    
#Recorrer todos los valores
for valores in diccionario.values():
    print(valores)
#Recorrer las claves y valores    
    print (clave, ":", "valor") 

