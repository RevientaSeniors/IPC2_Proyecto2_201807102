from Nodo import Nodo
from ListaDobleEnlazada import ListaDobleEnlazada
class Dron(Nodo):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.idDron = None
        self.alturaActual = None
        self.tiempoActual = 0
        self.estado = None
        self.letraActual = None
        self.posicion = None
        self.tiempoMaximo = 0
        self.listaEstados = ListaDobleEnlazada()

    def get_nombre(self):
        return self.nombre
    
    def set_tiempo_actual(self,tiempo):
        self.tiempoActual += tiempo

    def get_tiempo_actual(self):
        return self.tiempoActual
    
    def set_tiempo_maximo(self):
        self.tiempoMaximo = self.tiempoActual

    def time_zero(self):
        self.tiempoActual = 0

    def get_Tiempo_Maximo(self):
        return self.tiempoMaximo
    