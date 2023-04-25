import random
numero_secreto = int(random.random()*10)

encontrado=False
intentos = 0
while encontrado==False:
    numero_candidato = int(input("Introduce un número [0-10]:"))

    if numero_candidato==numero_secreto:
      
       encontrado=True
    else:
       print("El numero introducido no es el secreto")
    intentos+=1
    if intentos ==3:#detiene la ejecucion del bucle
        break
else:
    
print("Eres un gran adivino")