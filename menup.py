from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from gramaticas import bienvenida2
from Automatas import bautomatas


class menuprincipal():
    def __init__(self):
        self.win2 = tk.Toplevel()
        self.win2.resizable(True,False) # Redimensionar la ventana
        self.win2.title('..::BIENVENIDO::..') # Titulo de la ventana
        self.win2.geometry('1000x700') # Tamaño de la ventana
        self.Centrar(self.win2, 1000, 700) # Centrar la ventana
        self.win2.config(bg='#111111')
        self.Ventana() # Llamar a la ventana

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight() # Altura de la pantalla
        ancho_pantalla = r.winfo_screenwidth() # Ancho de la pantalla

        x = (ancho_pantalla // 2) - (ancho // 2) # Posicion de la ventana
        y = (altura_pantalla // 2) - (alto // 2) # Posicion de la ventana
        r.geometry(f'+{x}+{y}') # Posicion de la ventana

    def Ventana(self):
        self.frame = Frame(height=1000, width=700) # Se coloca sobre la ventana
        self.frame.config(bg='#102027')
        self.frame.pack(padx=10, pady=10)
        Label(self.win2, text="Menú Principal", font=('Times New Roman',15), fg='#000000', bg='#FFAC33', width=20).place(x=400, y=50)
     
        Button(self.win2, text="Módulo Gramaticas",command=bienvenida2, font=('Times New Roman',15), fg='#000000', bg='#FFAC33', width=15).place(x=425, y=240)
        Button(self.win2, text="Módulo Autómatas",command=bautomatas, font=('Times New Roman',15), fg='#000000', bg='#FFAC33', width=15).place(x=425, y=280)
        Button(self.win2, text="Exit",command=lambda:self.win2.destroy(), font=('Times New Roman',15), fg='#000000', bg='#FFAC33', width=15).place(x=425, y=360)

    


        self.frame.mainloop()