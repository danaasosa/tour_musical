import tkinter as tk
from tkinter import ttk
import json
import ruta_agregar
import tkinter.messagebox

combo = None  # Definir combo como una variable global

def ruta_user(nombre_ingresado):
    selected_item = combo.get()

    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/ruta.json','r') as file:
        data_ruta = json.load(file)

    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/usuarios.json','r') as file:
        data_user = json.load(file)

    for user in data_user['Usuarios']:
        if user['Nombre'] == nombre_ingresado:
            for ruta in data_ruta['Rutas']:
                if ruta['Nombre'] == selected_item:
                    user['Ruta'] = ruta
     
    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/usuarios.json','w') as file:
        json.dump(data_user,file, indent=4)

    # Mostrar ventana emergente con el mensaje
    tkinter.messagebox.showinfo("Ruta", "¡Ruta agregada con Exito!")

def crear_ruta(nombre_ingresado):
    ruta_agregar.crear_ruta(nombre_ingresado)

def salir(ventana):
    ventana.destroy()


def ruta_usuario(nombre_ingresado):

    global combo  # Acceder a la variable global combo

    # Crear una ventana
    ventanaRuta = tk.Tk()
    ventanaRuta.title("Rutas")
    ventanaRuta.geometry("750x690")

    # Agregar un fondo morado
    fondo_blanco = tk.Canvas(ventanaRuta, bg="white")
    fondo_blanco.pack(fill="both", expand=True)

    # Agregar un titulo
    titulo_label = tk.Label(fondo_blanco, text=f"{nombre_ingresado}, a continuación te mostraremos \nlas rutas sugeridads: ", font=("Monaco", 20), bg='white', fg='black')
    titulo_label.place(relx=0.5, rely=0.2, anchor="center")

    #Abrir json
    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/ruta.json','r') as file:
        data_ruta = json.load(file)
    
    nombres_rutas = []

    for ruta in data_ruta['Rutas']:
        nombres_rutas.append(ruta['Nombre'])
    
    # Crear una etiqueta y una lista desplegable

    etiqueta = tk.Label(fondo_blanco, text="Seleccione una opción:",font=('Mocano',15),bg='white',fg='black')
    etiqueta.place(relx=0.5, rely=0.4, anchor="center")

    combo = ttk.Combobox(fondo_blanco, values=nombres_rutas,width=30)
    combo.set("Rutas disponibles")
    combo.place(relx=0.5, rely=0.5, anchor="center")

    # Botón de agregar ruta 
    boton_continuar = tk.Button(fondo_blanco, text="Agregar ruta a mi usuario",command=lambda: ruta_user(nombre_ingresado))
    boton_continuar.place(relx=0.5, rely=0.6, anchor="center")

    # Botón para crear nueva ruta
    boton_info = tk.Button(fondo_blanco, text="Crear nueva ruta",command=lambda: crear_ruta(nombre_ingresado))
    boton_info.place(relx=0.5, rely=0.7, anchor="center")

    #Boton de continuar
    boton_continuar = tk.Button(fondo_blanco, text="Ver todos los eventos",command=lambda: salir(ventanaRuta))
    boton_continuar.place(relx=0.5, rely=0.8, anchor="center")

    ventanaRuta.mainloop()