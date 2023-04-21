import random
print (random.random()) #[0,1]
random.seed()
random.seed(1234)
print (random.random()) #[0,1]
print(random.randrange(10,20))
print(random.randrange(10,20,2))
print(random.randint(10,20))

lista = ["Javier", "Alba","Julian","Alba"]
print (random.choice(lista))
print (random.choices(lista, k=3))
print (random.sample(lista, k=3))