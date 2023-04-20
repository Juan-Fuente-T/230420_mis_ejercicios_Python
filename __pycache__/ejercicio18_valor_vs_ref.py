x=10
y=x
print(x, y)
x=12
print(x, y)#se asigna el valor simplemente

lx = [3,5]
ly = lx 
print(lx, ly)
lx.append(8)
print(lx, ly)#aqui no se asigna valor de uno a otro, se copia la lista

lx = [3,5]
ly = lx.copy()
print(lx, ly)
lx.append(8)

#todavia hay mas, ver ejercicio del profe