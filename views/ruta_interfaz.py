import json

class Ruta:
    def __init__(self, nombre, destinos ,id_ruta = None):
        self.nombre = nombre
        self.destinos = destinos
        if id_ruta is None:
            self.id_ruta = id(nombre)
        else:
            self.id_ruta = id_ruta
    
    def to_json(self):
        return {
            'ID':self.id_ruta,
            'Nombre':self.nombre,
            'Destino':self.destinos
        }