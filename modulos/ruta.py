import json

class Ruta:
    def __init__(self, nombre, destinos ,id_ruta = None):
        self.nombre = nombre
        self.destinos = destinos
        if id_ruta is None:
            self.id_ruta = id(nombre)
        else:
            self.id_ruta = id_ruta

    def __str__(self):
        return f"Ruta: {self.nombre}, Destinos: {self.destinos}"

    def agregar_destino(self, evento):
        self.destinos.append(evento.id_evento)

    def obtener_destinos(self):
        return self.destinos
    
    def to_json(self):
        return {
            'ID':self.id_ruta,
            'Nombre':self.nombre,
            'Destino':self.destinos
        }