#Importación de Tkinter
import tkinter as tk

#Creación y configuaración de la ventana 
ventana = tk.Tk()
ventana.title("Mi primer programa con Tkinter")
ventana.geometry("500x300")


#Etiqueta
etiqueta = tk.Label(text="hola", background="lightblue")

#Muestra la etiqueta de la ventana
etiqueta.pack()


#Bucle de la ventana
ventana.mainloop()

