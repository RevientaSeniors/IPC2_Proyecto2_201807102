from Nodo import Nodo
class Instruccion(Nodo):
    def __init__(self, dron, altura):
        super().__init__()
        self.dron = dron
        self.altura = altura

    def imprimir(self):
        print(f' instruccion para dron {self.dron} para altura {self.altura}')