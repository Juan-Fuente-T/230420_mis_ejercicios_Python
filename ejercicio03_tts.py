from gtts import gTTS
import os


#nombre = input("introduce tu nombre:") 
#edad = input("introduce tu edad:")
#mytext= f"Te llamas {nombre} y tienes {edad}años"
#audio = gTTS (text=mytext, lang="es", slow=False)
#audio.save("example.mp3")
#os.system("start example.mp3")*/

lista = ["lunes", "martes", "jueves", "Automovil"]
for item in lista:

audio = gTTS (text=mytext, lang="es", slow=False)
audio.save("example.mp3")
os.system("start example.mp3")
