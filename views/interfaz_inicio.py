import tkinter as tk
from tkinter import ttk

import interfaz_sesion 
import interfaz_registro

# Variable global para la imagen del logo
logo_inicio = None

def iniciar_sesion():
    interfaz_sesion.login()

def registrarse():
    interfaz_registro.registrar()

def inicio():

    # Crear una ventana
    ventana = tk.Tk()
    ventana.title("Inicio")

    # Configurar el tamaño de la ventana
    ventana.geometry("750x690")

    # Agregar un fondo morado
    fondo_morado = tk.Canvas(ventana, bg="purple4")
    fondo_morado.pack(fill="both", expand=True)

    # Agregar un logo
    logo = tk.PhotoImage(file="/Users/danaa.sosa/Downloads/Tour Musical/assets/imagenes/logo.png")
    logo_label = tk.Label(fondo_morado, image=logo)
    logo_label.pack(pady=20)

    # Agregar un mensaje de bienvenida
    bienvenida_label = tk.Label(fondo_morado, text="Bienvenido a Tour Musical APP", font=("Monaco", 20), bg='purple4', fg='white')
    bienvenida_label.pack()

    # Agregar botones
    boton_inicio = tk.Button(fondo_morado, text="Iniciar sesión", command=iniciar_sesion)
    boton_inicio.pack(pady=10)

    boton_registrarse = tk.Button(fondo_morado, text="Registrarse", command=registrarse)
    boton_registrarse.pack()

    # Iniciar la interfaz de usuario
    ventana.mainloop()

inicio()