import tkinter as tk
from tkinter import ttk
import json
import explorar_event
import tkinter.messagebox

combo = None  # Definir combo como una variable global

def agregar_evento(nombre_ingresado):
    selected_item = combo.get()

    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/usuarios.json','r') as file:
        usuarios = json.load(file)

    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/eventos.json','r') as file:
        eventos = json.load(file)
    
    for user in usuarios['Usuarios']:
        if user['Nombre'] == nombre_ingresado:
            hist_user = user['Historial Destinos']
            for evento in eventos['Eventos']:
                if evento['Nombre del evento'] == selected_item:
                    hist_user.append(evento['Evento id'])
                    user.update({'Historial Destinos':hist_user})
                    # Mostrar ventana emergente con el mensaje
                    tkinter.messagebox.showinfo("Evento Agregado", f"{nombre_ingresado}, {selected_item} fue agregado a tu historial")

    
    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/usuarios.json','w') as file:
        json.dump(usuarios, file, indent=4)

    

def explorar_eventos():
    selected_item = combo.get()
    explorar_event.mostrar_ventana_evento(selected_item)


def indice(nombre_ingresado):

    global combo  # Acceder a la variable global combo

    # Crear una ventana
    ventana = tk.Tk()
    ventana.title("Indice de Eventos")
    ventana.geometry("750x690")

    # Agregar un fondo morado
    fondo_morado = tk.Canvas(ventana, bg="purple4")
    fondo_morado.pack(fill="both", expand=True)

    # Agregar un titulo
    titulo_label = tk.Label(fondo_morado, text="Eventos resgistrados en nuestro sistema:", font=("Monaco", 20), bg='purple4', fg='white')
    titulo_label.place(relx=0.5, rely=0.2, anchor="center")

    # abrir archivo json para obtener los nombres de los eventos
    nombres_eventos = [] #lista vacia para guardar los nombres
    eventos_dicc = {} #dicc con los nombres y ids
    
    with open('data/eventos.json', 'r') as json_file:
        eventos = json.load(json_file)
        
    for evento in eventos["Eventos"]:
        nombres_eventos.append(evento.get('Nombre del evento'))
        eventos_dicc[evento.get('Nombre del evento')] = evento.get('Evento id')

    # Crear una etiqueta y una lista desplegable

    etiqueta = tk.Label(fondo_morado, text="Seleccione una opción:",font=('Mocano',15),bg='purple4')
    etiqueta.place(relx=0.5, rely=0.4, anchor="center")

    combo = ttk.Combobox(fondo_morado, values=nombres_eventos,width=30)
    combo.set("Desplega para ver todos los eventos")
    combo.bind("<<ComboboxSelected>>")  # Asociar una función de selección
    combo.place(relx=0.5, rely=0.5, anchor="center")

    # Botón para explorar el evento seleccionado
    boton_continuar = tk.Button(fondo_morado, text="Información del evento", command=explorar_eventos)
    boton_continuar.place(relx=0.5, rely=0.6, anchor="center")

    # Botón para agregar el evento seleccionado a la lista del usuario
    boton_select = tk.Button(fondo_morado, text="Agregar evento a mi lista",command=lambda: agregar_evento(nombre_ingresado))
    boton_select.place(relx=0.5, rely=0.7, anchor="center")

    ventana.mainloop()