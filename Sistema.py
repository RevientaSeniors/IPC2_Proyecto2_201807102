from Nodo import Nodo
class Sistema(Nodo):
    def __init__(self,nombre,altMax, cantiDrones):
        super().__init__()
        self.nombre = nombre
        self.altMax = altMax
        self.cantiDrones = cantiDrones

    def imprimir(self):
        print(f'SISTEMA CON NOMBRE {self.nombre}  altura maxima de {self.altMax} y cantidad de drones de {self.cantiDrones}')