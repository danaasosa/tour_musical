import random

class Review:
    def __init__(self, evento, usuario, calificacion, comentario, animo,id_review = None):
        self.evento = evento
        self.usuario = usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo
        if id_review is None:
            self.id_review = id(comentario)
        else:
            self.id_review = id_review
    
    def to_json(self):
        return {
            'ID Review': self.id_review,
            'ID Evento':self.evento,
            'ID Usuario':self.usuario,
            'Calificacion':self.calificacion,
            'Comentario': self.comentario,
            'Animo': self.animo
        }