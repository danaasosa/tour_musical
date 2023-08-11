import tkinter as tk
from tkinter import ttk
import json
import indice_eventos
from insertar_review import review
from explorar_event import mostrar_ventana_evento as mve
import tkintermapview
import interfaz_ruta

combo = None  # Definir combo como una variable global

def review_user(usuario_login):
    selected_item = combo.get()
    review(selected_item,usuario_login)

def continuar(nombre_ingresado):
    indice_eventos.indice(nombre_ingresado)

def ir_rutas(nombre_ingresado,ventanaHD):
    interfaz_ruta.ruta_usuario(nombre_ingresado)
    ventanaHD.destroy()

def mostrar_info():
    selected_item = combo.get()
    mve(selected_item) #Muestra la informacion del evento seleccionado

def historial_userDest(nombre_ingresado):

    global combo  # Acceder a la variable global combo

    # Crear una ventana
    ventanaHD = tk.Tk()
    ventanaHD.title("Historial del usuario")
    ventanaHD.geometry("750x690")

    # Agregar un fondo morado
    fondo_morado = tk.Canvas(ventanaHD, bg="purple4")
    fondo_morado.pack(fill="both", expand=True)

    # Agregar un titulo
    titulo_label = tk.Label(fondo_morado, text=f"{nombre_ingresado}, a continuación te mostraremos \nlos eventos en tu historial: ", font=("Monaco", 20), bg='purple4', fg='white')
    titulo_label.place(relx=0.5, rely=0.2, anchor="center")

    # abrir archivo json para obtener el historial de eventos
    nombres_eventos = [] #lista vacia para guardar los nombres

    with open('data/usuarios.json', 'r') as json_file:
        usuarios = json.load(json_file)
    
    with open('data/eventos.json', 'r') as json_file:
        eventos = json.load(json_file)

    for usuario in usuarios['Usuarios']:
        if usuario.get("Nombre") == nombre_ingresado:
            if len(usuario.get("Historial Destinos"))>0:
                for evento_id in usuario.get("Historial Destinos"):
                    for evento in eventos["Eventos"]:
                        if evento_id == evento.get("Evento id"):
                            nombres_eventos.append(evento.get('Nombre del evento'))
                usuario_login = usuario['ID']
            else:
                nombres_eventos.append('Aun no has asistido a ningún evento')

    
    # Crear una etiqueta y una lista desplegable

    etiqueta = tk.Label(fondo_morado, text="Seleccione una opción:",font=('Mocano',15),bg='purple4')
    etiqueta.place(relx=0.5, rely=0.4, anchor="center")

    combo = ttk.Combobox(fondo_morado, values=nombres_eventos,width=30)
    combo.set("Historial de eventos")
    combo.place(relx=0.5, rely=0.5, anchor="center")

    # Botón de insertar review
    boton_continuar = tk.Button(fondo_morado, text="Agregar una reseña",command=lambda: review_user(usuario_login))
    boton_continuar.place(relx=0.5, rely=0.6, anchor="center")

    # Botón para ver toda la informacion del evento
    boton_info = tk.Button(fondo_morado, text="Información del evento",command=mostrar_info)
    boton_info.place(relx=0.5, rely=0.7, anchor="center")

    #Boton de continuar
    boton_continuar = tk.Button(fondo_morado, text="Ver todos los eventos",command=lambda: continuar(nombre_ingresado))
    boton_continuar.place(relx=0.5, rely=0.8, anchor="center")

    # Botón de ir a rutas
    boton_continuar = tk.Button(fondo_morado, text="Rutas",command=lambda: ir_rutas(nombre_ingresado,ventanaHD))
    boton_continuar.place(relx=0.5, rely=0.9, anchor="center")

    ventanaHD.mainloop()