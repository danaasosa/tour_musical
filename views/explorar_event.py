import tkinter as tk
import json
from tkinter import ttk
from PIL import Image, ImageTk  # Para trabajar con imágenes
import map
import tkintermapview

def cerrar_ventana(ventana):
    ventana.destroy()

def mostrar_ventana_evento(evento_select):
    # Crear ventana
    ventana = tk.Toplevel()
    ventana.title("Detalles del Evento")
    ventana.geometry("750x800")

    # Agregar un fondo morado
    fondo_blanco = tk.Canvas(ventana, bg="white")
    fondo_blanco.pack(fill="both", expand=True)

    # Abrir archivo para json para ver la informacion del evento
    
    with open('data/eventos.json', 'r') as json_file:
        eventos = json.load(json_file)
        
    for evento in eventos["Eventos"]:
        if evento_select == evento.get('Nombre del evento'):
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

    label_imagen = tk.Label(fondo_blanco, image=imagen)
    label_imagen.pack(pady=10)

    # Mostrar información del evento en etiquetas
    label_titulo = tk.Label(fondo_blanco, text=f"{datos_evento['Nombre del evento']} - {datos_evento['Artista']}", font=("Helvetica", 15,'bold'),bg='white',fg='black')
    label_titulo.pack()
    label_ubi = tk.Label(fondo_blanco, text=f"Ubicacion {ubi_evento['Nombre']}\n{ubi_evento['Direccion']}", font=("Helvetica", 15,'bold'),bg='white',fg='black')
    label_ubi.pack()
    label_hora = tk.Label(fondo_blanco, text=f"Apertura de Puertas: {datos_evento['Hora de inicio']} \nFinaliza: {datos_evento['Hora de finalizacion']}", font=("Helvetica", 15,'bold'),bg='white',fg='black')
    label_hora.pack()
    label_descripcion = tk.Label(fondo_blanco, text=f"Descripción: {datos_evento['Descripcion']}", wraplength=380, font=("Helvetica", 15,'bold'),bg='white',fg='black')
    label_descripcion.pack()

    # Agregar botones
    boton_salir = tk.Button(fondo_blanco, text="CERRAR", command=lambda: cerrar_ventana(ventana))
    boton_salir.pack(pady=10)

    ventana.mainloop()