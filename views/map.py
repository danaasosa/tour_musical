import tkinter as tk
import tkintermapview
from tkinter import ttk
import json

map_widget = None
my_slider = None
my_entry = None
combo = None

def lookup(coord_eventos): #Permite ir directamente a la direccion del evento selecionado
    evento = combo.get()
    c = coord_eventos.get(evento)
    cordenada1 = c[0]
    cordenada2 = c[1]
    map_widget.set_position(cordenada1,cordenada2,evento,marker=True)
    my_slider.config(value=9)

def slide(e):
    map_widget.set_zoom(my_slider.get())

def mapa_event(event_select = None):

    #Variables globales
    global map_widget
    global my_slider
    global my_entry
    global combo

    # Crear una ventana
    ventanaMap = tk.Tk()
    ventanaMap.title("MAPA")
    ventanaMap.geometry('900x800')


    my_label = tk.LabelFrame(ventanaMap)
    my_label.pack(pady=20)

    map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600, corner_radius=0)
    map_widget.pack()

    #Set coordenadas
    #Abrir archivos json

    with open('data/eventos.json', 'r') as json_file:
        eventos = json.load(json_file)

    with open('data/ubicacion.json', 'r') as json_file:
        ubicaciones = json.load(json_file)

    coord_eventos = {} #Lista vacia de cordenadas
    nombres_eventos = []
        
    for evento in eventos["Eventos"]:
        for ubi in ubicaciones['Ubicaciones']:
            if evento['Ubicacion id']==ubi['ID']:
                coord_eventos[evento['Nombre del evento']] = ubi['Coordenadas']
            if event_select is None:
                 #Set direccion en el mapa
                 map_widget.set_position(-24.788333333333, -65.410555555556,text='SALTA',marker=True)
            else:
                if evento['Nombre del evento']==event_select:
                    if evento['Ubicacion id']==ubi['ID']:
                        list_coord = ubi['Coordenadas']
                        coordenada_set1 = list_coord[0]
                        coordenada_set2 = list_coord[1]
                        #Set coordenada del evento seleccionado previamente
                        map_widget.set_position(coordenada_set1,coordenada_set2,text=event_select,marker=True)
        nombres_eventos.append(evento['Nombre del evento'])
    

    #Set zoom
    map_widget.set_zoom(20)

    map_widget.pack()

    my_frame = tk.LabelFrame(ventanaMap)
    my_frame.pack(padx=20,pady=10)

    combo = ttk.Combobox(ventanaMap, values=nombres_eventos,width=30)
    combo.set("Busca un evento en el mapa")
    combo.place(relx=0.3, rely=0.02, anchor='w')

    my_button = tk.Button(my_frame,text="Abrir en el mapa",font=('Monaco',18,'bold'),fg = 'black',bg='black',command=lambda: lookup(coord_eventos))
    my_button.grid(row=0,column=1,padx=10)

    my_slider = ttk.Scale(my_frame,from_=4, to=20,orient='horizontal',command=slide,value=20,length=220)
    my_slider.grid(row=0,column=2,padx=10)

    ventanaMap.mainloop()