from laptop_Business import Laptop_Business
#Crear interfaz
import tkinter  as tk
from tkinter import ttk
#Imagenes instalar con el comando: pip install PILLOW
from PIL import Image, ImageTk
#Genera un valor aleatorio
import random

class CrearLaptop:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes = ["C:\\Users\\ADRIAN CHICAIZA\\Desktop\\Modulo5\\img\\1.jpg",
                         "C:\\Users\\ADRIAN CHICAIZA\\Desktop\\Modulo5\\img\\2.jpg",
                         "C:\\Users\\ADRIAN CHICAIZA\\Desktop\\Modulo5\\img\\3.jpg",
                         "C:\\Users\\ADRIAN CHICAIZA\\Desktop\\Modulo5\\img\\4.jpg",
                         "C:\\Users\\ADRIAN CHICAIZA\\Desktop\\Modulo5\\img\\5.jpg",
                         ]
        root.title("Crear Laptop_Business")
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(row=0, column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1)

        ttk.Label(self.root, text="Procesador").grid(row=1, column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable= self.procesador).grid(row=1, column=1)

        ttk.Label(self.root, text="Memoria").grid(row=2, column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable= self.memoria).grid(row=2, column=1)

        ttk.Label(self.root, text="Espacio Disco").grid(row=3, column=0)
        self.espacio_disco = tk.StringVar()
        ttk.Entry(self.root, textvariable= self.espacio_disco).grid(row=3, column=1)

        ttk.Label(self.root, text="Duracion Bateria").grid(row=4, column=0)
        self.duracion_bateria = tk.StringVar()
        ttk.Entry(self.root, textvariable= self.duracion_bateria).grid(row=4, column=1)

        ttk.Label(self.root, text="Precio").grid(row=5, column=0)
        self.precio = tk.StringVar()
        ttk.Entry(self.root, textvariable= self.precio).grid(row=5, column=1)

        ttk.Button(self.root, text="Crear Laptops", command=self.crear_laptop_Business).grid(row=6, column=0)

        self.mostrar_laptops = tk.Text(self.root, height=10, width=50)
        self.mostrar_laptops.grid(row=7, column=0, columnspan=2)

        self.canva = tk.Canvas(self.root, width=200, height=200)
        self.canva.grid(row=1,column=3, rowspan=6 )

    def crear_laptop_Business(self):
        nueva_laptop= Laptop_Business(self.marca.get(), self.procesador.get(), self.memoria.get(), self.espacio_disco.get(), self.duracion_bateria.get(), self.precio.get())
        self.laptops.append(nueva_laptop)
        self.mostrar_laptops.insert(tk.END, f"{nueva_laptop}")
        self.mostrar_imagen_aleatoria()
        
    def mostrar_imagen_aleatoria(self):
        imagen_path = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen =imagen.resize((200,200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)

        self.canva.create_image(0,0, anchor=tk.NW, image = photo)
        self.canva.image = photo

        pass
root = tk.Tk()
app = CrearLaptop(root)
root.mainloop()
