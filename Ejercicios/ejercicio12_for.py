lista=[8,4,13,10,15,25]
#bucle normal
for elemento in lista:
    print(elemento)
    if elemento==15:
        break #Detiene el bucle
else:#Solo si se recorre la lista entera
    print("Else")
#bucle con slicing
for elemento in lista[1::2]:
    print(elemento, end=":")
#bucle for con range 100 y 0 decreciente
for i in range(100,-1,-1):
    print(i, end="-")
print()
