import tkinter as tk
from menup import menuprincipal

root = tk.Tk()
root.geometry('700x300')
root.title('Proyecto2.')
b=tk.Label(root, text="Bienvenidos", font=('Times New Roman',15), fg='#000000', bg='#DCDCDC', width=20).place(x=250, y=50)
c=tk.Label(root, text="Lenguajes Formales y de Programación N", font=('Times New Roman',15), fg='#000000', bg='#DCDCDC', width=50).place(x=75, y=80)
d=tk.Label(root, text="Henry Alexander García Montúfar", font=('Times New Roman',15), fg='#000000', bg='#DCDCDC', width=50).place(x=75, y=110)
e=tk.Label(root, text="Carnet:201407049", font=('Times New Roman',15), fg='#000000', bg='#DCDCDC', width=50).place(x=75, y=140)


def MostrarVentana():
    a=menuprincipal()
    
    

def OcultarVentana():
    root.withdraw()
    root.after(3000, MostrarVentana)


root.after(3000, OcultarVentana) # Dentro de 3s más o menos inicia la función de eliminación u desaparición de la ventana
root.mainloop()
