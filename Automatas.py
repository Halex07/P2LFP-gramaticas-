from tkinter import *
from tkinter import ttk
from distutils.cmd import Command
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from auto import *
from gra import *
import functools
from Gramatica import *
from ListaGramaticas import *

class bautomatas():
    def __init__(self):
        self.gramatica = []
        self.error = []
        self.winA = tk.Toplevel()
        self.winA.resizable(True,False) # Redimensionar la ventana
        self.winA.title('..::ADF::..') # Titulo de la ventana
        self.winA.geometry('1000x700') # Tamaño de la ventana
        self.Centrar2(self.winA, 1000, 700) # Centrar la ventana
        self.winA.config(bg='#102027')
        self.Ventana3() # Llamar a la ventana

    def Centrar2(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight() # Altura de la pantalla
        ancho_pantalla = r.winfo_screenwidth() # Ancho de la pantalla

        

        x = (ancho_pantalla // 2) - (ancho // 2) # Posicion de la ventana
        y = (altura_pantalla // 2) - (alto // 2) # Posicion de la ventana
        r.geometry(f'+{x}+{y}') # Posicion de la ventana

    def Ventana3(self):
        self.cont1 = Frame(height=1000, width=700) # Se coloca sobre la ventana
        self.cont1.config(bg='#707070')
        self.cont1.pack(padx=10, pady=10)
        Label(self.winA, text="...:::...Módulo de Automatas...:::...", font=('Times New Roman',15), fg='#000000', bg='#FFAC33', width=52).place(x=200, y=20)
        Button(self.winA, text="Cargar Archivo",command=self.cargar, font=('Times New Roman',15), fg='#000000', bg='#FFAC33', width=15).place(x=425, y=240)
        Button(self.winA, text="Información General",command=opcion1, font=('Times New Roman',15), fg='#000000', bg='#FFAC33', width=15).place(x=425, y=280)
        Button(self.winA, text="Ruta de validación",command=opcion2, font=('Times New Roman',15), fg='#000000', bg='#FFAC33', width=15).place(x=425, y=320)
        Button(self.winA, text="Paso a Paso",command=opcion2, font=('Times New Roman',15), fg='#000000', bg='#FFAC33', width=15).place(x=425, y=360)
        Button(self.winA, text="Validar Cadena",command=opcion3, font=('Times New Roman',15), fg='#000000', bg='#FFAC33', width=15).place(x=425, y=360)
        Button(self.winA, text="Una Pasada",command=opcion3, font=('Times New Roman',15), fg='#000000', bg='#FFAC33', width=15).place(x=425, y=360)
        Button(self.winA, text="Atrás",command=lambda:self.winA.destroy(), font=('Times New Roman',15), fg='#000000', bg='#FFAC33', width=15).place(x=425, y=360)


        
    def ExisteGramatica(self, AFD):
        for afd in self.gramatica:
            if afd.nombre == AFD:
                print('Existe una gramatica con ese nombre')
                return True
        return False

    def EstaVacio(self):
        if len(self.gramatica) == 0:
            return True
        else:
            return False

    def EliminarAFD(self, nombre):
        for afd in self.gramatica:
            if afd.nombre == nombre:
                self.gramatica.remove(afd)
                print('Gramatica eliminada')

    def Agregar(self, AFD):
        if not self.ExisteGramatica(AFD.nombre):
            self.gramatica.append(AFD)
        else:
            '''Ya se manda mensaje desde el otro metodo'''

    def MostrarGramaticas(self):
        for afd in self.gramatica:
            print(afd.nombre)

    def cargar(self):
        ruta = filedialog.askopenfilename(title = "Seleccionar Archivo",filetypes = ((".* Files","*.*"),))
        #Buffer.cargar_buffer(import_file_path)
        automatas = open(ruta, 'r+')
        listaglc.CargarGramaticas(ruta)
        
        noL = 0  # Numero de linea
        for linea in automatas.readlines():
            noL += 1
            linea = linea.replace('\n', '')

            if noL == 1:  # Ingresando titulo al automata
                if not self.ExisteGramatica(linea):
                    EnCreacion = Gramatica(linea)
                    
                else:
                    self.EliminarAFD(linea)
                    EnCreacion = Gramatica(linea)
                   
            elif noL == 2:  # Ingresando alfabeto del automata
                contador = 0
                for d in linea.split(';'):
                    print(d)
                    if contador == 0:
                        for alfa in d.split(','):
                            EnCreacion.AgregarEstados(alfa)
                            EnCreacion.cadenanotermianles = d
                    elif contador == 1:
                        for alfa in d.split(','):
                            EnCreacion.IngresarAlfabeto(alfa)
                        EnCreacion.cadenaterminales = d
                    elif contador == 2:
                        EnCreacion.inicial = d
                    contador += 1
            elif linea == '*':
                print(' ')
                if EnCreacion.EsLibreDeContexto:
                    self.gramatica.append(EnCreacion)
                    print('Automata agregado correctamente')
                    self.ImprimirAutomata(EnCreacion)

                else:
                    print('No es una gramatica libre del contexto, no sera agregada')
                    self.error.append(['Nombre de la gramatica:  ' + str(EnCreacion.nombre), 'error, no se cargo no es una gramatica de tipo 2 o Libre del contexto'])
                    ListaGramatica.reporteError(self)
                noL = 0
            else:
                EnCreacion.AgregarTransicion(linea)
        automatas.close()

    def ImprimirAutomata(self, EnCreacion):

        print('Nombre:', EnCreacion.nombre)
        print('No terminales:', EnCreacion.cadenanotermianles)
        print('Terminales: ', EnCreacion.cadenaterminales)
        print('No terminal inicial:', EnCreacion.inicial)
        print('Producciones:')
        n = 0
        for estado in EnCreacion.noterminales:
            n += 1
            no = 1
            for transicion in estado.transiciones:
                if no == 1:
                    print("producion "+str(n)+': '+estado.estado, '->', transicion)
                else:
                    print("\t"+"\t"+"\t"+"\t"+'|', transicion)
                no += 1

    def DevolverADP(self, nombre):
        for adp in self.gramatica:
            if adp.nombre == nombre:
                return adp
        return False

    def reporteError(self):
        contenido = ''
        htmFile = open("Reporte_Gramaticas" + ".html", "w", encoding='utf8')
        htmFile.write("""<!DOCTYPE HTML PUBLIC"
                   <html>
                   <head>
                       <title>Reporte de errores</title>
                    <meta charset="utf-8">
                 <meta name="viewport" content="width=device-width, initial-scale=1">
                 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
                 <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
                   </head>
                   <body>
                   <div class="container">
                 <h2>Reporte de errores</h2>
                 <p>Lista de errores</p>            
                 <table class="table">
                   <thead>
                     <tr>
                      <th>nombre</th>
                       <th>razon</th>
                       
                     </tr>
                   </thead>
                   """)
        for i in range(len(self.error)):
            contenido += (" <tbody>"
                          "<td>" + str(self.error[i][0]) + "</td>"
                          "<td>" + str(self.error[i][1]) + "</td>"
                          
                          "</tbody>")
        htmFile.write(contenido)
        htmFile.write("""
                 </table>
            </div>
                </body>
                </html>""")
        htmFile.close