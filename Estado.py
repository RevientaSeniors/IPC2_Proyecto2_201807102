from Nodo import Nodo
class Estado(Nodo):
    def __init__(self,tiempo, estado):
        super().__init__()
        self.tiempo = tiempo
        self.estado = estado

    def set_estado(self, estado):
        self.estado = estado