import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def convertir():
    print("Convirtiendo:::")
   #hacer esto
    messagebox.showinfo("Traductor v1.0", dia")
    

ventana = tk.Tk()
ventana.title("Conversor a Gallego")
ventana.config(width=800, height=500)

label_dia = ttk.Label(text="Nombre en castellano:")
label_dia.place(x=20, y=20)

input_dia = ttk.Entry()
input_dia.place(x=150, y= 20, width=122)

button_traducir = ttk.Button(text="Traducir", command= "Convertir")
button_traducir.place(x=20, y= 60)

ventana.mainloop()