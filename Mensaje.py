from Nodo import Nodo
from ListaDobleEnlazada import ListaDobleEnlazada
class Mensaje(Nodo):
    def __init__(self, nombre, sistema):
        super().__init__()
        self.nombre = nombre
        self.sistema = sistema
        self.decifrado = None
        self.listaInstrucciones = ListaDobleEnlazada()

    def imprimir(self):
        print(f'MENSAJE ORDENADO ALFABETICAMENTE nombre {self.nombre} apunta a sistema {self.sistema} con lista inst')
        self.listaInstrucciones.mostrar2()

    def get_sistema(self):
        return self.sistema
    
    def get_nombre(self):
        return self.nombre
    
    def get_instrucciones(self):
        return self.listaInstrucciones
    
    
        