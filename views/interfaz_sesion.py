import tkinter as tk
import json
import tkinter.messagebox
import historial_user


def verificar_usuario(entry_nombre, entry_apellido, resultado_label,ventanaLogin):
    nombre_ingresado = entry_nombre.get()
    apellido_ingresado = entry_apellido.get()

    with open('data/usuarios.json', 'r') as json_file:
        usuarios = json.load(json_file)

    for usuario in usuarios['Usuarios']:
        if usuario['Nombre'] == nombre_ingresado and usuario['Apellido'] == apellido_ingresado:
            # Mostrar ventana emergente con el mensaje
            tkinter.messagebox.showinfo("Inicio Sesion", f"{nombre_ingresado} ¡BIENVENID@!")

            ventanaLogin.destroy() #Cerrar la ventana de Login una vez iniciada la sesion

            # Abrir una nueva ventana aquí
            historial_user.historial_userDest(nombre_ingresado)

            return

    resultado_label.config(text="Usuario inválido", font=('Monaco',20,'bold'), bg='white', fg="red")
    resultado_label.place(x=0, y=400, width=320)

def login():

    # Crear una ventana
    ventanaLogin = tk.Tk()
    ventanaLogin.title("Interfaz de Login")

    # Configurar el tamaño de la ventana
    ventanaLogin.geometry("320x500")

    # Agregar un fondo morado
    fondo_morado = tk.Canvas(ventanaLogin, bg="purple4")
    fondo_morado.pack(fill="both", expand=True)

    # Etiqueta en la parte superior con letra en cursiva
    titulo_label = tk.Label(fondo_morado, text="Inicio de Sesion", font=('Monaco', 18), bg='purple4', fg='white')
    titulo_label.place(relx=0.5, rely=0.2, anchor="center")

    # Etiqueta y entrada para nombre
    label_nombre = tk.Label(fondo_morado, text="Nombre:", font=('Monaco', 15), bg='purple4')
    label_nombre.place(relx=0.5, rely=0.4, anchor="center")
    entry_nombre = tk.Entry(fondo_morado, font=('Arial', 15), fg='black', bg='white')
    entry_nombre.place(relx=0.5, rely=0.45, anchor="center")

    # Etiqueta y entrada para apellido
    label_apellido = tk.Label(fondo_morado, text="Apellido:", font=('Monaco', 15), bg='purple4')
    label_apellido.place(relx=0.5, rely=0.55, anchor="center")
    entry_apellido = tk.Entry(fondo_morado, font=('Arial', 15), fg='black', bg='white')
    entry_apellido.place(relx=0.5, rely=0.6, anchor="center")

    # Etiqueta para mostrar el resultado de la verificación
    resultado_label = tk.Label(fondo_morado, text="", font=("Helvetica", 12))
    resultado_label.pack()

    # Botón de verificación
    boton_verificar = tk.Button(fondo_morado, text="Ingresar", command=lambda: verificar_usuario(entry_nombre, entry_apellido, resultado_label,ventanaLogin), bg='purple4')
    boton_verificar.place(relx=0.5, rely=0.7, anchor="center")

    # Iniciar la interfaz de usuario
    ventanaLogin.mainloop()