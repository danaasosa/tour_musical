import tkinter as tk
from tkinter import ttk
import json
from ruta_interfaz import Ruta
import tkinter.messagebox

combo = None

def agregar_destino(destinos_id):
    selected_item = combo.get()

    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/eventos.json','r') as file:
        data_eventos = json.load(file)

    for evento in data_eventos['Eventos']:
        if evento['Nombre del evento']==selected_item:
            destinos_id.append(evento['Evento id'])

    # Mostrar ventana emergente con el mensaje
    tkinter.messagebox.showinfo("Destino", "¡Destino agregado con Exito!")

    return destinos_id


def guardar_ruta(nombre_user,entry_nombre,destinos_id):

    #Creacion de la ruta
    nombre_ingresado = entry_nombre.get()
    destinos = destinos_id

    ruta = Ruta(nombre_ingresado,destinos)

    # Mostrar ventana emergente con el mensaje
    tkinter.messagebox.showinfo("Ruta", "¡Ruta guardada con Exito!")

    #Obtener los datos de un archivo json y luego editarla y agregar el nuevo user al archivo
    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/ruta.json', 'r') as json_file:
        datos = json.load(json_file)
    
    datos['Rutas'].append(ruta.to_json())

    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/ruta.json','w') as json_file:
        json.dump(datos,json_file,indent=4)

    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/usuarios.json','r') as file:
        data_user = json.load(file)

    for user in data_user['Usuarios']:
        if user['Nombre'] == nombre_user:
            if user['Ruta'] is None:
                user['Rutas'] = []
                user['Rutas'].append(ruta.to_json())
            else:
                lista_rutas = user['Rutas']
                lista_rutas.append(ruta.to_json())
     
    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/usuarios.json','w') as file:
        json.dump(data_user,file, indent=4)
    
    # Mostrar ventana emergente con el mensaje
    tkinter.messagebox.showinfo("Ruta User", "¡Ruta agregada a tu usuario con Exito!")

def crear_ruta(nombre_user):

    global combo

    destinos_id = []

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Crear Ruta")
    root.geometry("580x680")

    # Crear widgets y elementos de la interfaz
    label_nombre = tk.Label(root, text="Nombre de la ruta:")
    label_nombre.place(relx=0.5, rely=0.4, anchor="center")
    entry_nombre = tk.Entry(root)
    entry_nombre.place(relx=0.5, rely=0.45, anchor="center")

    label_destinos = tk.Label(root, text="Destinos:")
    label_destinos.place(relx=0.5, rely=0.5, anchor="center")

    #Abrir archivo json
    with open('data/eventos.json', 'r') as json_file:
        eventos = json.load(json_file)
    
    nombres_eventos = []
        
    for evento in eventos["Eventos"]:
        nombres_eventos.append(evento['Nombre del evento'])
       
    combo = ttk.Combobox(root, values=nombres_eventos,width=30)
    combo.set("Eventos disponibles")
    combo.place(relx=0.5, rely=0.55, anchor="center")

    boton_agregar = tk.Button(root, text="Agregar Destino", command=lambda: agregar_destino(destinos_id))
    boton_agregar.place(relx=0.5, rely=0.6, anchor="center")

    boton_guardar = tk.Button(root, text="Guardar Ruta", command=lambda: guardar_ruta(nombre_user,entry_nombre,destinos_id))
    boton_guardar.place(relx=0.5, rely=0.67, anchor="center")

    # Iniciar la interfaz
    root.mainloop()
