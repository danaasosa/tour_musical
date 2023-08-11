import json

class Ubicación:
    def __init__(self, nombre, direccion, coordenadas = [],id_ubi = None):
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas
        if id_ubi is None:
            self.id_ubi = id(nombre)
        else:
            self.id_ubi = id_ubi

    def __str__(self):
        return f"{self.nombre}, {self.direccion}, Coordenadas: {self.coordenadas}"
    
    def to_json(self):
        return {
            'ID': self.id_ubi,
            'Nombre': self.nombre,
            'Direccion': self.direccion,
            'Coordenadas': self.coordenadas
        }