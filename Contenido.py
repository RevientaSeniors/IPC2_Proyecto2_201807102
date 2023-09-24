from Nodo import Nodo
from ListaDobleEnlazada import ListaDobleEnlazada
from Altura import Altura
from Dron import Dron

class Contenido(Nodo):
    def __init__(self, dron):
        super().__init__()
        self.dron = dron
        self.listaAlturas = ListaDobleEnlazada()

    def imprimir(self):
        print(f' con el dron {self.dron} y alturas ')
        self.listaAlturas.mostrar2()
    
    