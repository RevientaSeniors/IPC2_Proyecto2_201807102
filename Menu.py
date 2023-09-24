from os import sep, system
import os
import xml.etree.ElementTree as Et
import tkinter as tk
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
        self.master.title('DRON SYSTEM')

        # Definiendo el tamaño de la ventana y centrándola en la pantalla
        window_width = 1280
        window_height = 720
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_coordinate = (screen_width/2) - (window_width/2)
        y_coordinate = (screen_height/2) - (window_height/2)
        self.master.geometry(f'{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}')

        self.master.configure(bg='gray7')

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

        self.graph_btn = tk.Button(master, text='CARGAR UN ARCHIVO', command=self.cargarArchivo, **style_settings)
        self.graph_btn.pack(pady=5)
        #self.graph_btn.place(x=1070,y=180)

        self.delete_btn = tk.Button(master, text='GESTION DE DRONES', command=lambda: self.gestionDrones(), **style_settings)
        self.delete_btn.pack(pady=5)
        
        # self.update_btn = tk.Button(master, text='Actualizar elemento', command=lambda: self.actualizar(self.prompt_choice("Escoge un ID"), self.prompt_choice("Escribe el nuevo nombre")), **style_settings)
        # self.update_btn.pack(pady=5)
        
        # Inicializando el label
        self.elements_label = tk.Label(master, text="", **style_settings)
        self.elements_label.pack(pady=5)
        
        #imagen
        self.canvas = tk.Canvas(master, width=920, height=540, bg='gray20', scrollregion=(0,0,1000,1000))
        self.canvas.pack(side=tk.LEFT, pady=5)
        
        self.scroll_y = tk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
        self.scroll_y.pack(side=tk.LEFT, fill="y")
        self.canvas.configure(yscrollcommand=self.scroll_y.set)
        
        self.image_label = tk.Label(self.canvas, bg='gray20')
        self.canvas.create_window((0,0), window=self.image_label, anchor="nw")
        
        self.image_label.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.opcion = 0
        self.listaDrones = ListaDobleEnlazada()
        self.listaSistemas = ListaDobleEnlazada()
        self.listaMensajes = ListaDobleEnlazada()
        self.estado = True


    # def showMenu(self):
    #     while(self.estado):
    #         self.limpiarPantalla()
    #         print("────────────── MENÚ ─────────────── ")
    #         print("│ 1. INICIALIZAR                   │")
    #         print("│ 2. CARGAR UN ARCHIVO             │")
    #         print("│ 3. GENERAR UN ARCHIVO            │")
    #         print("│ 4. GESTIÓN DE DRONES             │")
    #         print("│ 5. GESTIÓN DE SISTEMAS DE DRONES │")
    #         print("│ 6. GESTIÓN DE MENSAJES           │")
    #         print("│ 7. AYUDA                         │")
    #         print("│ 8. SALIR                         │")
    #         print("────────────────────────────────────")
    #         self.opcion = int(input("Elija su opción: "))
    #         if(self.opcion == 1):
    #             self.listaDrones.inicializar()  
    #             input('¡Sistema Inicializado! \n Presione ENTER para continuar...')
    #         elif self.opcion == 2:
    #             self.cargarArchivo()
    #         elif self.opcion == 3:
    #             print ("ES DRONX ARRIBA DE DRONY?")
    #             print("baaaaa">"AB")
    #             input()
    #         elif self.opcion == 8:
    #             salir = input('¿Seguro que quiere salir? Y/N \n')   
    #             if salir == 'Y':
    #                 self.estado = False
                
    #         else:
    #             input('Valor inválido \n Presione ENTER para continuar')

    def cargarArchivo(self):
        fileName = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
        if(fileName):
            self.listaDrones.inicializar()
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
                    #self.listaSistemas.agregarAlFinal(Sistema(nombre, altM, cantDrones))
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
                    self.listaMensajes.agregarOrdenado(nuevoMensaje)  


            self.listaMensajes.mostrar2()
            messagebox.showinfo("!Carga exitosa¡", "Los datos se han cargado exitosamente")
        else:
            messagebox.showerror("¡ERROR!", f"Ningún archivo seleccionado") 

    def inicializarPrograma(self):
        self.listaDrones.inicializar()
        messagebox.showinfo("¡Proceso Exitoso!", "El programa se inicializó exitosamente")

    def gestionDrones(self):
        listado = self.listaDrones.mostrar()
        nuevodron = tk.simpledialog.askstring("Listado Drones", listado, parent=self.master)
        if nuevodron:
            nombre = self.listaDrones.buscar(nuevodron)
            if nombre:
               messagebox.showerror("¡ERROR!", f"El Dron con nombre {nuevodron} ya existe") 
            else:
                messagebox.showinfo("¡Agregado!", f"El Dron con nombre {nuevodron} ha sido agregado")
                self.listaDrones.agregarOrdenado(Dron(nuevodron))
            

    def limpiarPantalla(self):
        system('cls')