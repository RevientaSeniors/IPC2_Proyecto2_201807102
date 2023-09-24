from Nodo import Nodo
from Contenido import Contenido
from ListaDobleEnlazada import ListaDobleEnlazada
class Sistema(Nodo):
    def __init__(self,nombre,altMax, cantiDrones):
        super().__init__()
        self.nombre = nombre
        self.altMax = altMax
        self.cantiDrones = cantiDrones
        self.listaContenido = ListaDobleEnlazada()
    
    def imprimir(self):
        print(f'SISTEMA CON NOMBRE {self.nombre}  \n')
        self.listaContenido.mostrar2()
