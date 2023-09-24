from Nodo import Nodo
class Altura(Nodo):
    def __init__(self, valor, letra):
        super().__init__()
        self.valor = valor
        self.letra = letra


    def imprimir(self):
        print(f' altura con valor {self.valor} y letra {self.letra} ')
        