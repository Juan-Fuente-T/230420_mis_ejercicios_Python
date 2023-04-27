lista =[1,2,3,4,5,6,7,8,9]
lista_dobles = [numero * 2 for numero in lista ]
print(lista)
print(lista_dobles)
generador_triples = [numero * 3 for numero in lista ]
print(type(generador_triples))
for triple in generador_triples:
    print(triple, end="-")
