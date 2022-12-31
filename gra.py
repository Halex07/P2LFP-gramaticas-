from ListaGramaticas import *
from ListaAP import *
listaglc = ListaGramatica()
listaAP = ListaAutomatas()
from Lgramaticas import Gramatica, Producciones
lista_nombres_Gramatica = []
lista_Gramaticas = []
lista_Automatas = []


def opcion1():

    listaglc.MostrarGramaticas()
    eleccion = "Grm2"
    automata = listaglc.DevolverADP(eleccion)
    
    listaglc.ImprimirAutomata(automata)
    
    listaglc.MostrarGramaticas()
    eleccion = input('Por favor ingrese el nombre de la gramatica de la cual desea su automata equivalente...')
    automata = listaglc.DevolverADP(eleccion)
    automata.AutomataEquivalente()
    
    print('Cargando gramaticas a la lista')
    listaAP.CargarAFDs('automatas.ap')
    print('Los automatas disponibles son: ')
    listaAP.MostrarAPs()
    eleccion = input('Por favor ingrese el nombre del automata con el que desea evaluar...')
    automata = listaAP.DevolverADP(eleccion)
    seguir = True

    while seguir:
                print('Si no desea validar mas cadenas ingrese "SALIR"')
                cadena = input('Por favor ingrese la cadena que desea evaluar con ' + automata.nombre + '...')
                try:
                    if cadena == 'SALIR':
                        seguir = False
                    else:
                        automata.ValidarCadenaMostrandoPasos(cadena)
                except:
                    print('No eligio un automata correcto')
    

    listaAP.CargarAFDs('automatas.ap')

    print('Los automatas disponibles son: ')
    listaAP.MostrarAPs()
    eleccion = input('Por favor ingrese el nombre del automata con el que desea evaluar...')
    automata = listaAP.DevolverADP(eleccion)
    seguir = True
    while seguir:
                print('Si no desea validar mas cadenas ingrese "SALIR"')
                cadena = input('Por favor ingrese la cadena que desea evaluar con ' + automata.nombre + '...')
                try:
                    if cadena == 'SALIR':
                        seguir = False
                    else:
                        automata.ValidarCadenaConReporte(cadena)
                except:
                    print('No eligio un automata correcto')



