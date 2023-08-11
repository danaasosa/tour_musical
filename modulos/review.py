class Review:
    def __init__(self, evento, usuario, calificacion, comentario, animo,id_review = None):
        self.evento = evento
        self.usuario = usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo
        if id_review is None:
            self.id_review = evento + usuario
        else:
            self.id_review = id_review

    def __str__(self):
        return f"Review de {self.usuario} para {self.evento}: Calificación {self.calificacion}, Comentario: '{self.comentario}', Ánimo: {self.animo}"

    def obtener_evento(self):
        return self.evento

    def obtener_usuario(self):
        return self.usuario

    def obtener_calificacion(self):
        return self.calificacion

    def obtener_comentario(self):
        return self.comentario

    def obtener_animo(self):
        return self.animo
    
    def to_json(self):
        return {
            'ID Review': self.id_review,
            'ID Evento':self.evento,
            'ID Usuario':self.usuario,
            'Calificacion':self.calificacion,
            'Comentario': self.comentario,
            'Animo': self.animo
        }