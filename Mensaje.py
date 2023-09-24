from Nodo import Nodo
from Instruccion import Instruccion
from ListaDobleEnlazada import ListaDobleEnlazada
class Mensaje(Nodo):
    def __init__(self, nombre, sistema):
        super().__init__()
        self.nombre = nombre
        self.sistema = sistema
        self.listaInstrucciones = ListaDobleEnlazada()
    

    def imprimir(self):
        print(f'MENSAJE ORDENADO ALFABETICAMENTE nombre {self.nombre} apunta a sistema {self.sistema} con lista inst')
        self.listaInstrucciones.mostrar2()