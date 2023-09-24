class ListaDobleEnlazada:
    def __init__(self):
        self.inicio = None
        self.final = None

    def inicializar(self):
        self.inicio = None
        self.final = None

    def agregarAlFinal(self,data):
        if self.inicio is None:
            self.inicio = data
            self.final = data
        else:
            actual = self.inicio
            while actual.siguiente is not None:
                actual = actual.siguiente
            data.anterior = actual
            self.final = data
            actual.siguiente = data

    def agregarOrdenado(self,data):
        if self.inicio is None:
            self.inicio = data
            self.final = data
        else:
            actual = self.inicio
            while actual:
                if data.nombre < actual.nombre:
                    if actual.anterior is  None:
                        actual.anterior = data
                        #data.siguiente = actual
                    else:
                        data.anterior = actual.anterior
                        actual.anterior = data
                        data.anterior.siguiente = data
                    data.siguiente = actual
                    
                    if data.anterior is None:
                        self.inicio = data
                    actual = actual.siguiente
                    break
                if actual.siguiente is None:
                    actual.siguiente = data
                    data.anterior = actual
                    self.final = data
                    break
                actual = actual.siguiente

    def buscar(self,nombre):
        actual = self.inicio
        while actual:
            if(nombre == actual.nombre):
                return nombre
            actual = actual.siguiente
        return None

    def mostrar(self):
        cadena = 'LISTADO DE DRONES ORDENADO \n'
        actual = self.inicio
        while actual:
            cadena += actual.get_Nombre()
            cadena +='\n'
            actual = actual.siguiente 
        cadena +='¿Desea agregar un nuevo Dron?'
        return cadena
    
    def mostrar2(self):
        actual = self.inicio
        while actual:
            actual.imprimir()
            actual = actual.siguiente 
