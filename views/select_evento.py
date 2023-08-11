import tkinter as tk
import json
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk  # Para trabajar con imágenes
from usuario_interfaz import Usuario

combo = None  # Definir combo como una variable global

def agregar_evento(selected_item,nombre_ingresado):

    # abrir archivo json para obtener el historial de eventos y nos id de los eventos

    with open('data/usuarios.json', 'r') as json_file:
        usuarios = json.load(json_file)

    with open('data/eventos.json', 'r') as json_file:
        eventos = json.load(json_file)
    
    for user in usuarios['Usuarios']:
        if user['Nombre'] == nombre_ingresado:
            hist_eventos = user['Historial Destinos']
            for evento in eventos['Eventos']:
                if evento['Nombre del evento'] == selected_item:
                    hist_eventos.append(evento['Evento id'])
                    user.update({'Historial Destinos': hist_eventos})

    # Mostrar ventana emergente con el mensaje
    tkinter.messagebox.showinfo("Evento Agregado", f"Se agrego a tu historial de eventos {selected_item}")
    

def ventana_evento(selected_item,nombre_ingresado):


    # Crear ventana
    ventana = tk.Toplevel()
    ventana.title("Evento")
    ventana.geometry("750x800")

    # Agregar un fondo morado
    fondo_gris = tk.Canvas(ventana, bg="gray")
    fondo_gris.pack(fill="both", expand=True)

    # Abrir archivo para json para ver la informacion del evento
    
    with open('data/eventos.json', 'r') as json_file:
        eventos = json.load(json_file)
        
    for evento in eventos["Eventos"]:
        if selected_item == evento.get('Nombre del evento'):
            datos_evento = evento
    
    # Abrir archivo para json para ver la informacion de la ubicacion del evento
    with open('data/ubicacion.json', 'r') as json_file:
        ubicacion = json.load(json_file)

    for ubi in ubicacion['Ubicaciones']:
        if datos_evento['Ubicacion id'] == ubi.get('ID'):
            ubi_evento = ubi

    # Cargar la imagen y mostrarla en la parte superior de la ventana
    imagen = Image.open(datos_evento["URL imagen"])
    imagen = imagen.resize((500, 500), Image.LANCZOS)
    imagen = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(fondo_gris, image=imagen)
    label_imagen.pack(pady=10)

    # Mostrar información del evento en etiquetas
    label_titulo = tk.Label(fondo_gris, text=f"{datos_evento['Nombre del evento']} - {datos_evento['Artista']}", font=("Helvetica", 15,'bold'),bg='white',fg='black')
    label_titulo.pack()
    label_ubi = tk.Label(fondo_gris, text=f"Ubicacion {ubi_evento['Nombre']}\n{ubi_evento['Direccion']}", font=("Helvetica", 15,'bold'),bg='white',fg='black')
    label_ubi.pack()
    label_hora = tk.Label(fondo_gris, text=f"Apertura de Puertas: {datos_evento['Hora de inicio']} \nFinaliza: {datos_evento['Hora de finalizacion']}", font=("Helvetica", 15,'bold'),bg='white',fg='black')
    label_hora.pack()
    label_descripcion = tk.Label(fondo_gris, text=f"Descripción: {datos_evento['Descripcion']}", wraplength=380, font=("Helvetica", 15,'bold'),bg='white',fg='black')
    label_descripcion.pack()

    # Botón para explorar el evento seleccionado
    boton_select = tk.Button(fondo_gris, text="Seleccionar evento",command=agregar_evento(selected_item,nombre_ingresado))
    boton_select.place(relx=0.5, rely=0.7, anchor="center")

    ventana.mainloop()
