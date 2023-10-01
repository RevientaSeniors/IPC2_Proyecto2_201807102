from Nodo import Nodo
class Instruccion(Nodo):
    def __init__(self, dron, altura):
        super().__init__()
        self.dron = dron
        self.altura = int(altura)
        self.tiempo = None

    def imprimir(self):
        print(f' instruccion para dron {self.dron} para altura {self.altura}')


    def get_dron(self):
        return self.dron
    
    def get_altura(self):
        return self.altura
    
    
    
