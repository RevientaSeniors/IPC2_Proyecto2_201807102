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
                return actual
            actual = actual.siguiente
        return None
    
    def buscarLetra(self,altura):
        actual = self.inicio
        while actual:
            if(str(altura) == actual.valor):
                return actual.letra
            actual = actual.siguiente
        return None

    def mostrarDrones(self):
        cadena = 'LISTADO DE DRONES ORDENADO \n'
        actual = self.inicio
        while actual:
            cadena += actual.get_nombre()
            cadena +='\n'
            actual = actual.siguiente 
        cadena +='¿Desea agregar un nuevo Dron?'
        return cadena
    
    def mostrarMensajes(self):
        cadena = 'LISTADO DE MENSAJES \n'
        actual = self.inicio
        while actual:
            mensajes = actual.get_mensajes()
            mensaje_actual = mensajes.inicio
            while mensaje_actual:
                #actual.get_tabla_estados(mensaje_actual.get_nombre())
                cadena += f'- Nombre Mensaje: {mensaje_actual.get_nombre()}\n'
                cadena +=f'Mensaje {actual.get_mensaje(mensaje_actual.get_nombre())}\n'
                instrucciones = mensaje_actual.get_instrucciones()
                instruccion = instrucciones.inicio
                while(instruccion):
                    contenidos = actual.listaContenido
                    contenido = contenidos.inicio
                    while(contenido):
                        if(contenido.nombre == instruccion.get_dron()):
                            alturas = contenido.listaAlturas
                            altura = alturas.inicio
                            while(altura):
                                if(int(altura.valor) == instruccion.get_altura()):
                                    cadena += f'Dron: {instruccion.get_dron()} a {instruccion.get_altura()} metros (Representa la {altura.letra}) \n'
                                altura = altura.siguiente
                        contenido = contenido.siguiente
                    instruccion = instruccion.siguiente
                mensaje_actual = mensaje_actual.siguiente
            actual = actual.siguiente 
        return(cadena)
    
    def getMensaje(self):
        actual = self.inicio
        mensajes = actual.get_mensajes()
        mensaje_actual = mensajes.inicio
        while mensaje_actual:
            cadena += f'- Nombre Mensaje: {mensaje_actual.get_nombre()}\n'
            cadena += actual.get_mensaje(mensaje_actual.get_nombre())
            mensaje_actual = mensaje_actual.siguiente
    
    # def mostrarInstrucciones(self):
    #     actual = self.inicio
    #     cadena =''
    #     while actual:
    #         cadena+= f' Dron: {actual.get_dron()} a {actual.get_altura()} metros. \n'
    #         actual = actual.siguiente 
    #     return cadena
    
    def mostrar2(self):
        actual = self.inicio
        while actual:
            actual.imprimir()
            actual = actual.siguiente 

    def generarXML(self):
        sistema = self.inicio
        cadena = '<?xml version="1.0"?><respuesta><listaMensajes>'
        while(sistema):
            mensajes = sistema.listadoMensajes
            mensaje = mensajes.inicio
            while(mensaje):
                sistema.get_tabla_estados(mensaje.nombre)
                cadena +=f'<mensaje nombre="{mensaje.nombre}">'
                cadena +=f'<sistemaDrones>{sistema.nombre}</sistemaDrones>'
                cadena +=f'<tiempoOptimo>{sistema.maxTiempo}</tiempoOptimo>'
                cadena +=f'<mensajeRecibido>{sistema.get_mensaje(mensaje.nombre)}</mensajeRecibido>'
                cadena +=f'<instrucciones>'
                for i in range(1, sistema.maxTiempo+1):
                    cadena +=f'<tiempo valor="{i}"><acciones>'
                    drones = sistema.listaDrones
                    dron  = drones.inicio
                    while(dron):
                        estados = dron.listaEstados
                        estado = estados.inicio
                        while(estado):
                            if(int(estado.tiempo) == i):
                                cadena +=f'<dron nombre="{dron.nombre}"> {estado.estado} </dron>'
                            estado = estado.siguiente
                        dron = dron.siguiente
                    cadena +='</acciones></tiempo>'
                mensaje = mensaje.siguiente
                cadena +=f'</instrucciones>'
            cadena +=f'</mensaje>'
            sistema.inicializarTiempoDrones()
            sistema = sistema.siguiente
        cadena +=f'</listaMensajes></respuesta>'
        return cadena
    