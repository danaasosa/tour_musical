import json
import datetime
import locale
from ubicacion import Ubicación

locale.setlocale(locale.LC_TIME,"es_ES")

class Evento:
    def __init__(self, nombre,artista,genero,ubicacion,hora_inicio,hora_fin,descripcion,imagen,id_evento=None):
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubi = ubicacion.id_ubi
        self.hora_inicio = datetime.datetime.strptime(hora_inicio, '%Y/%m/%d %H:%M')
        self.hora_fin = datetime.datetime.strptime(hora_fin, '%Y/%m/%d %H:%M')
        self.descripcion = descripcion
        self.imagen = imagen
        if id_evento is None:
            self.id_evento = id(nombre)
        else:
            self.id_evento = id_evento

    def __str__(self):
        return f"{self.nombre} - Inicio: {self.hora_inicio.isoformat()}, Finaliza: {self.hora_fin.isoformat()}"

    def to_json(self):
        return {
        "Evento id": self.id_evento,
        "Nombre del evento":self.nombre,
        "Artista":self.artista,
        "Genero Musical":self.genero,
        "Ubicacion id": self.id_ubi,
        "Hora de inicio": self.hora_inicio.isoformat(),
        "Hora de finalizacion": self.hora_fin.isoformat(),
        "Descripcion":self.descripcion,
        "URL imagen":self.imagen
    }
