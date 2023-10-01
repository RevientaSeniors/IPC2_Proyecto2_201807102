from os import sep, system
from tkinter.constants import END, INSERT
import os
import xml.etree.ElementTree as Et
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog, PhotoImage
from Dron import Dron
from Sistema import Sistema
from Contenido import Contenido
from Altura import Altura
from Mensaje import Mensaje
from Instruccion import Instruccion
from ListaDobleEnlazada import ListaDobleEnlazada


class Menu():
    def __init__(self,master):
        self.master = master
        cuadroTextoEditar = tk.Text(self.master)
        self.master.title('DRON SYSTEM')
        pantallaGestion = master

        # Definiendo el tamaño de la ventana y centrándola en la pantalla
        window_width = 1280
        window_height = 720
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_coordinate = (screen_width/2) - (window_width/2)
        y_coordinate = (screen_height/2) - (window_height/2)
        self.master.geometry(f'{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}')

        self.master.configure(bg='gray7')
        #cuadroTextoEditar.place(x=640,y=300, width= 640, height=540)
        #cuadroTextoEditar.configure(borderwidth=3, relief="solid")

        style_settings = {
            "bg": "yellow2",
            "fg": "black",
            "padx": 10,
            "pady": 5,
            "font": ("Helvetica", 10)
        }

        # Botones y widgets
        self.load_btn = tk.Button(master, text='INICIALIZAR', command=self.inicializarPrograma, **style_settings)
        self.load_btn.pack(pady=5)  # El padding 'pady' añade espacio entre los botones
        #self.load_btn.place(x=1070,y=90)

        self.cargar_btn = tk.Button(master, text='CARGAR UN ARCHIVO', command=self.cargarArchivo, **style_settings)
        self.cargar_btn.pack(pady=5)
        #self.graph_btn.place(x=1070,y=180)

        self.generar_btn = tk.Button(master, text='GENERAR UN ARCHIVO', command=self.generarArchivo, **style_settings)
        self.generar_btn.pack(pady=5)

        self.gestionDrones_btn = tk.Button(master, text='GESTIÓN DE DRONES', command=lambda: self.gestionDrones(), **style_settings)
        self.gestionDrones_btn.pack(pady=5)

        self.gestionSistema_btn = tk.Button(master, text='GESTIÓN DE SISTEMAS DE DRONES', command=self.generarGrafica, **style_settings)
        self.gestionSistema_btn.pack(pady=5)

        self.gestion_msj_btn = tk.Button(master, text='GESTIÓN DE MENSAJES', command=self.gestionMensajes, **style_settings)
        self.gestion_msj_btn.pack(pady=5)

        self.ayuda_btn = tk.Button(master, text='AYUDA', command=self.datos, **style_settings)
        self.ayuda_btn.pack(pady=5)
        
        # self.update_btn = tk.Button(master, text='Actualizar elemento', command=lambda: self.actualizar(self.prompt_choice("Escoge un ID"), self.prompt_choice("Escribe el nuevo nombre")), **style_settings)
        # self.update_btn.pack(pady=5)
        
        # Inicializando el label
        #self.elements_label = tk.Label(master, text="", **style_settings)
        #self.elements_label.pack(pady=5)
        
        #imagen
        self.canvas = tk.Canvas(master, width=1280, height=540, bg='gray20', scrollregion=(0,0,1000,1000))
        self.canvas.pack(side=tk.LEFT, pady=5)
        
        self.scroll_y = tk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
        self.scroll_y.pack(side=tk.LEFT, fill="y")
        self.canvas.configure(yscrollcommand=self.scroll_y.set)
        
        self.image_label = tk.Label(self.canvas, bg='gray20')
        self.canvas.create_window((0,0), window=self.image_label, anchor="nw")
        
        self.image_label.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.listaDrones = ListaDobleEnlazada()
        self.listaSistemas = ListaDobleEnlazada()
        self.listaMensajes = ListaDobleEnlazada()
        self.listaConfiguraciones = ListaDobleEnlazada()
        self.centinela =True

    def cargarArchivo(self):
        fileName = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
        if(fileName):
            self.listaDrones.inicializar()
            self.listaMensajes.inicializar()
            self.listaSistemas.inicializar()
            self.centinela = True
            tree = Et.parse(fileName)
            root = tree.getroot()

            for listaDrones in root.findall('listaDrones'):
                for dron in  listaDrones.findall('dron'):
                    nuevoDron = Dron(dron.text)
                    self.listaDrones.agregarOrdenado(nuevoDron)
            
            for sistemas in root.findall('listaSistemasDrones'):
                for sistema in  sistemas.findall('sistemaDrones'):
                    nombre = sistema.get('nombre')
                    altM = sistema.find('alturaMaxima').text
                    cantDrones = sistema.find('cantidadDrones').text
                    nuevoSitema = Sistema(nombre,altM, cantDrones)
                    for contenido in sistema.findall('contenido'):
                        dron = contenido.find('dron').text
                        nuevoContenido = Contenido(dron)
                        nuevoSitema.listaContenido.agregarAlFinal(nuevoContenido)
                        for alturas in contenido.findall('alturas'):
                            for altura in alturas.findall('altura'):
                                valor = altura.get('valor')
                                letra = altura.text
                                nuevaAltura = Altura(valor,letra)
                                nuevoContenido.listaAlturas.agregarAlFinal(nuevaAltura)
                    self.listaSistemas.agregarAlFinal(nuevoSitema)

            for mensajes in root.findall('listaMensajes'):
                for mensaje in mensajes.findall('Mensaje'):
                    nombre = mensaje.get('nombre')
                    sistemaDrones = mensaje.find('sistemaDrones').text
                    nuevoMensaje = Mensaje(nombre, sistemaDrones)
                    for instrucciones in mensaje.findall('instrucciones'):
                        for instruccion in instrucciones.findall('instruccion'):
                            dron = instruccion.get('dron')
                            altura = instruccion.text
                            nuevaInstruccion = Instruccion(dron, altura)
                            nuevoMensaje.listaInstrucciones.agregarAlFinal(nuevaInstruccion)
                    sistema = self.listaSistemas.buscar(sistemaDrones)
                    sistema.listadoMensajes.agregarOrdenado(nuevoMensaje)
                    sistema.set_drones(self.listaDrones)
                    #self.listaMensajes.agregarOrdenado(nuevoMensaje)  

            #self.listaConfiguraciones.agregarAlFinal(self.listaMensajes)
            #self.listaConfiguraciones.agregarAlFinal(self.listaSistemas)
            #self.listaConfiguraciones.agregarAlFinal(self.listaDrones)
            #self.listaSistemas.mostrarMensajes()
            messagebox.showinfo("!Carga exitosa¡", "Los datos se han cargado exitosamente")
        else:
            messagebox.showerror("¡ERROR!", f"Ningún archivo seleccionado") 

    def inicializarPrograma(self):
        self.listaDrones.inicializar()
        messagebox.showinfo("¡Proceso Exitoso!", "El programa se inicializó exitosamente")

    def gestionDrones(self):
        listado = self.listaDrones.mostrarDrones()
        nuevodron = tk.simpledialog.askstring("Listado Drones", listado, parent=self.master)
        if nuevodron:
            dron = self.listaDrones.buscar(nuevodron)
            if dron:
               messagebox.showerror("¡ERROR!", f"El Dron con nombre {nuevodron} ya existe") 
            else:
                messagebox.showinfo("¡Agregado!", f"El Dron con nombre {nuevodron} ha sido agregado")
                self.listaDrones.agregarOrdenado(Dron(nuevodron))

    def generarArchivo(self):
        nombre = tk.simpledialog.askstring("Listado Drones", "Escribe el nombre para el documento de salida", parent=self.master)
        f = open(f"{nombre}.xml",'w')
        f.write(self.listaSistemas.generarXML())
        f.close
        messagebox.showinfo("¡Generado!", f"El archivo de salida {nombre} ha sido generado")

    def generarGrafica(self):
        sistema = self.listaSistemas.inicio
        if(self.centinela):
            while(sistema):
                doc = sistema.nombre
                dot_string = 'digraph G {\n'
                dot_string += sistema.to_dot()
                dot_string += "}\n"
                with open(f"{doc}.dot", "w") as archivo:
                    archivo.write(dot_string)
                os.system(f"dot -Tpng {doc}.dot -o {doc}.png")
                sistema = sistema.siguiente
            self.centinela = False
            messagebox.showinfo("¡Generado!", "El archivo de graficos  ha sido generado")    
        else:
            nombre = tk.simpledialog.askstring("Grafica", "Escribe el nombre de la grafica para mostrar", parent=self.master)
            img = PhotoImage(file=f'{nombre}.png')
            self.image_label.config(image=img)
            self.image_label.image = img  

    def gestionMensajes(self):
        ventana_secundaria = tk.Toplevel()
        cuadro = tk.Text(ventana_secundaria)
        ventana_secundaria.title("Gestión de Mensajes")
        ventana_secundaria.config(width=520, height=310)
        cuadro.place(x=10,y=100, width= 500, height=200)
        cuadro.configure(borderwidth=3, relief="solid")
        lista_msj_btn = ttk.Button(ventana_secundaria, text="Listado de mensajes", command=lambda: cuadro.insert(INSERT,self.listaSistemas.mostrarMensajes()) )
        lista_msj_btn.place(x=80, y=50)
        instrucciones_btn = ttk.Button(ventana_secundaria, text="Instrucciones", command=lambda: cuadro.insert(INSERT,self.instrucciones()))
        instrucciones_btn.place(x=340, y=50)

    def instrucciones(self):
        cadena = ''
        nombre = tk.simpledialog.askstring("Listado Mensajes", '¿SISTEMA del mensaje a mostrar?', parent=self.master)
        sistema = self.listaSistemas.buscar(nombre)
        if(sistema):
            cadena += f'-NOMBRE SISTEMA: {sistema.nombre}\n'
            mensajes = sistema.get_mensajes()
            mensaje = mensajes.inicio
            while(mensaje):
                sistema.get_tabla_estados(mensaje.nombre)
                cadena +=f' Mensaje a enviar: {sistema.get_mensaje(mensaje.nombre)}\n'
                mensaje = mensaje.siguiente
            cadena +=f'  En un tiempo optimo = {sistema.maxTiempo}\n'
            sistema.inicializarTiempoDrones()
            doc = f'ins_{sistema.nombre}'
            dot_string = 'digraph G {\n'
            dot_string += sistema.to_ins()
            dot_string += "}\n"
            with open(f"{doc}.dot", "w") as archivo:
                archivo.write(dot_string)
            os.system(f"dot -Tpng {doc}.dot -o {doc}.png")
            img = PhotoImage(file=f'ins_{sistema.nombre}.png')
            self.image_label.config(image=img)
            self.image_label.image = img
            messagebox.showinfo("¡Generado!", "El archivo de instrucciones  ha sido generado")
        else:
            messagebox.showerror("¡ERROR!", f"Sistema no existe") 
        return cadena

    def datos(self):
        ventana_secundaria = tk.Toplevel()
        cuadro = tk.Text(ventana_secundaria)
        ventana_secundaria.title("Gestión de Mensajes")
        ventana_secundaria.config(width=520, height=310)
        cuadro.place(x=10,y=100, width= 500, height=200)
        cuadro.configure(borderwidth=3, relief="solid")
        cuadro.insert(INSERT,' Kenneth Emanuel Solís Ramírez \n201807102\nIntroducción a la programación y computación 2 Seccion A\n4to Semestre\nhttps://github.com/RevientaSeniors/IPC2_Proyecto2_201807102')

    def limpiarPantalla(self):
        system('cls')