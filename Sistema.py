from Nodo import Nodo
from Contenido import Contenido
from Estado import Estado
from ListaDobleEnlazada import ListaDobleEnlazada
class Sistema(Nodo):
    def __init__(self,nombre,altMax, cantiDrones):
        super().__init__()
        self.nombre = nombre
        self.altMax = altMax
        self.maxTiempo = 0
        self.cantiDrones = cantiDrones
        self.listaContenido = ListaDobleEnlazada()
        self.listadoMensajes = ListaDobleEnlazada()
        self.listaDrones = ListaDobleEnlazada()
    
    def imprimir(self):
        print(f'SISTEMA CON NOMBRE {self.nombre}  \n')
        self.listaContenido.mostrar2()
        self.listadoMensajes.mostrar2()

    def set_drones(self, listaDrones):
        self.listaDrones = listaDrones


    def get_mensajes(self):
        return self.listadoMensajes
    
    def get_mensaje(self,nombre):
        decododificado = ''
        mensaje = self.listadoMensajes.buscar(nombre)
        instrucciones = mensaje.get_instrucciones()
        instruccion = instrucciones.inicio
        while(instruccion):
            dron = self.listaDrones.buscar(instruccion.get_dron())
            contenido = self.listaContenido.buscar(dron.get_nombre())
            decododificado += contenido.listaAlturas.buscarLetra(instruccion.get_altura())
            instruccion = instruccion.siguiente
        return decododificado
    
    def get_tabla_estados(self,nombre):
        mensaje = self.listadoMensajes.buscar(nombre)
        instrucciones = mensaje.get_instrucciones()
        instruccion = instrucciones.inicio
        dron = self.listaDrones.inicio
        while(dron):
            while(instruccion):
                if(dron.nombre == instruccion.dron):
                    for j in range(1, instruccion.get_altura()+2):
                        nuevoEstado= None
                        if(j == instruccion.get_altura()+1):
                            if dron.get_tiempo_actual()<j:
                                nuevoEstado = Estado(j,'EMITIR LUZ')
                            else:
                                nuevoEstado = Estado(1+dron.get_tiempo_actual(), 'EMITIR LUZ')
                        else:
                            if dron.get_tiempo_actual()<j:
                                nuevoEstado = Estado(j,'SUBIR')
                            else:
                                nuevoEstado = Estado(1+dron.get_tiempo_actual(), 'SUBIR')
                        #print(f"se guardó al dron {dron.nombre} el valor {nuevoEstado.estado} en el tiempo {nuevoEstado.tiempo} con sistema {self.nombre}")
                        dron.listaEstados.agregarAlFinal(nuevoEstado)
                        dron.set_tiempo_actual(1) 
                        dron.set_tiempo_maximo()
                instruccion = instruccion.siguiente
            instruccion = instrucciones.inicio
            self.set_maxTiempo(dron.get_Tiempo_Maximo())
            dron = dron.siguiente
        

    def inicializarTiempoDrones(self):
        dron = self.listaDrones.inicio
        while(dron):
            # estado = dron.listaEstados.inicio
            # while(estado):
            #     if estado.estado == 'EMITIR LUZ':
            #         dronSiguiente = dron.siguiente
            #         estadoSiguiente = dronSiguiente.listaEstados.inicio
            #         while(estadoSiguiente):
            #             if estadoSiguiente.estado == 'EMITIR LUZ':
            #                  if(estado.tiempo == estadoSiguiente.tiempo):
            #                      estadoSiguiente.set_estado('ESPERAR')
            #                      estadoSiguiente.siguiente.set_estado('EMITIR LUZ')
            #             estadoSiguiente = estadoSiguiente.siguiente
            #     estado = estado.siguiente
            dron.listaEstados.inicio = None
            dron.time_zero()
            dron = dron.siguiente

    def set_maxTiempo(self,max):
        if(max > self.maxTiempo):
            self.maxTiempo = max

    def to_dot(self):
        cadena = '"elemento_1" [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD>ALTURA</TD>'
        contenidos = self.listaContenido
        contenido = contenidos.inicio
        while(contenido):
            cadena +=f'<TD>{contenido.nombre}</TD>'
            contenido = contenido.siguiente
        cadena +='</TR>'
        
        for i in range(1, int(self.altMax)+1):
            cadena +=f'<TR><TD>{i}</TD>'
            contenido = contenidos.inicio
            while(contenido):
                alturas= contenido.listaAlturas
                altura = alturas.inicio
                while(altura): 
                    if(int(altura.valor) == i):
                       cadena+=f'<TD>{altura.letra}</TD>' 
                    altura = altura.siguiente
                contenido = contenido.siguiente
            cadena +='</TR>'
        cadena +='</TABLE>>, shape=plain];'
        return cadena
    
    def to_ins(self):
        cadena = '"elemento_1" [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD>DRON</TD><TD>INSTRUCCION</TD></TR>'
        mensaje_actual = self.listadoMensajes.inicio
        while mensaje_actual:
            instrucciones = mensaje_actual.get_instrucciones()
            instruccion = instrucciones.inicio
            while(instruccion):
                contenidos = self.listaContenido
                contenido = contenidos.inicio
                while(contenido):
                    if(contenido.nombre == instruccion.get_dron()):
                        alturas = contenido.listaAlturas
                        altura = alturas.inicio
                        while(altura):
                            if(int(altura.valor) == instruccion.get_altura()):
                                cadena += f'<TR><TD>{instruccion.get_dron()}</TD> <TD>mover a {instruccion.get_altura()} metros (Representa la {altura.letra})</TD></TR>\n'
                            altura = altura.siguiente
                    contenido = contenido.siguiente
                instruccion = instruccion.siguiente
            mensaje_actual = mensaje_actual.siguiente
        cadena +='</TABLE>>, shape=plain];'
        return(cadena)
        