import tkinter as tk
import json
import tkinter.messagebox

from usuario_interfaz import Usuario


def ingresar_usuario(entry_nombre, entry_apellido,ventanaRegis):
    #Creacion del usuario
    nombre_ingresado = entry_nombre.get()
    apellido_ingresado = entry_apellido.get()

    user = Usuario(nombre_ingresado,apellido_ingresado)

    # Mostrar ventana emergente con el mensaje
    tkinter.messagebox.showinfo("Registro Exitoso", "¡Bienvenido a Tour Musical APP!")

    ventanaRegis.destroy()

    #Obtener los datos de un archivo json y luego editarla y agregar el nuevo user al archivo
    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/usuarios.json', 'r') as json_file:
        datos = json.load(json_file)
    
    datos['Usuarios'].append(user.to_json())

    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/usuarios.json','w') as json_file:
        json.dump(datos,json_file,indent=4)

def registrar():

    # Crear una ventana
    ventanaRegis = tk.Tk()
    ventanaRegis.title("Interfaz de Registro de Usuario")

    # Configurar el tamaño de la ventana
    ventanaRegis.geometry("620x480")

    # Agregar un fondo morado
    fondo_morado = tk.Canvas(ventanaRegis, bg="purple4")
    fondo_morado.pack(fill="both", expand=True)

    # Etiqueta en la parte superior con letra en cursiva
    titulo_label = tk.Label(fondo_morado, text="Te invitamos a registrarte en TOUR MUSICAL APP", font=('Monaco', 20), bg='purple4', fg='white')
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
    boton_verificar = tk.Button(fondo_morado, text="Registrar", command=lambda: ingresar_usuario(entry_nombre, entry_apellido,ventanaRegis), bg='purple4')
    boton_verificar.place(relx=0.5, rely=0.7, anchor="center")

    # Iniciar la interfaz de usuario
    ventanaRegis.mainloop()