from Nodo import Nodo
class Dron(Nodo):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.idDron = None
        self.alturaActual = None
        self.tiempoActual = None
        self.estado = None
        self.letraActual = None
        self.posicion = None

    def get_Nombre(self):
        return self.nombre