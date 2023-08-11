import tkinter as tk
from tkinter import ttk
import json
import tkinter.messagebox
from review_interfaz import Review

def agregar(event,usuario_login,entry_calif, entry_coment,entry_animo,ventanaReview):

    # Creacion de review
    calificacion = entry_calif.get()
    comentario = entry_coment.get()
    animo = entry_animo.get()

    #Abrir archivo json para obtener el id del evento
    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/eventos.json','r') as file: 
        eventos = json.load(file)
    
    for evento in eventos['Eventos']:
        if evento['Nombre del evento']==event:
            evento_id = evento['Evento id']
    
    review_new = Review(evento_id,usuario_login,calificacion,comentario,animo)

    # Abrir archivo json para guardar la review
    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/reviews.json','r') as file: 
        review = json.load(file)
    
    reviews = review['Reviews']
    reviews.append(review_new.to_json())
    
    data = {}
    data['Reviews'] = reviews

    with open('/Users/danaa.sosa/Downloads/Tour Musical/data/reviews.json','w') as file: 
        json.dump(data, file, indent=4)

    # Mostrar ventana emergente con el mensaje
    tkinter.messagebox.showinfo("Review", "¡Gracias por tu reseña!")

    ventanaReview.destroy()


def review(event,usuario_login):

    # Crear una ventana
    ventanaReview = tk.Tk()
    ventanaReview.title("Insertar Review")

    # Configurar el tamaño de la ventana
    ventanaReview.geometry("800x580")

    # Agregar un fondo morado
    fondo_morado = tk.Canvas(ventanaReview, bg="purple4")
    fondo_morado.pack(fill="both", expand=True)

    # Etiqueta en la parte superior con letra en cursiva
    titulo_label = tk.Label(fondo_morado, text=f"Te invitamos a dejar una reseña de {event}", font=('Monaco', 20), bg='purple4', fg='white')
    titulo_label.place(relx=0.5, rely=0.2, anchor="center")

    # Etiqueta y entradas
    label_calificacion = tk.Label(fondo_morado, text="Calificacion del 1 al 5 - siento 5 la nota mas alta:", font=('Monaco', 15), bg='purple4')
    label_calificacion.place(relx=0.5, rely=0.3, anchor="center")
    entry_calif = tk.Entry(fondo_morado, font=('Arial', 15), fg='black', bg='white')
    entry_calif.place(relx=0.5, rely=0.4, anchor="center")

    label_coment = tk.Label(fondo_morado, text="Comentario:", font=('Monaco', 15), bg='purple4')
    label_coment.place(relx=0.5, rely=0.5, anchor="center")
    entry_coment = tk.Entry(fondo_morado, font=('Arial', 15), fg='black', bg='white')
    entry_coment.place(relx=0.5, rely=0.6, anchor="center")

    label_animo = tk.Label(fondo_morado, text="Animo (Positivo o Negativo):", font=('Monaco', 15), bg='purple4')
    label_animo.place(relx=0.5, rely=0.7, anchor="center")
    entry_animo = tk.Entry(fondo_morado, font=('Arial', 15), fg='black', bg='white')
    entry_animo.place(relx=0.5, rely=0.8, anchor="center")

    # Botón de agregar review
    boton_verificar = tk.Button(fondo_morado, text="Agregar Review", command=lambda: agregar(event,usuario_login,entry_calif, entry_coment,entry_animo,ventanaReview), bg='purple4')
    boton_verificar.place(relx=0.5, rely=0.9, anchor="center")

    # Iniciar la interfaz de usuario
    ventanaReview.mainloop()    