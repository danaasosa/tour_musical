class Usuario:
    
    def __init__(self, nombre, apellido, id_usuario = None):
        self.nombre = nombre
        self.apellido = apellido
        self.historial_eventos = []
        if id_usuario is None:
            self.id_usuario = id(nombre)
        else:
            self.id_usuario = id_usuario

    def __str__(self):
        return f"Nombre: {self.nombre} \nApellido: {self.apellido}"

    def agregar_evento_historial(self, evento):
        self.historial_eventos.append(evento.id_evento)

    def obtener_historial_eventos(self):
        return self.historial_eventos
    
    def to_json(self):
        return {
            'ID': self.id_usuario,
            'Nombre':self.nombre,
            'Apellido':self.apellido,
            'Historial Destinos':self.historial_eventos
        }