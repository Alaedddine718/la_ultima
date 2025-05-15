import uuid
from datetime import datetime, timedelta

class Encuesta:
    def __init__(self, pregunta, opciones, duracion_segundos, tipo="simple"):
        self.id = str(uuid.uuid4())
        self.pregunta = pregunta
        self.opciones = opciones  # lista de opciones
        self.votos = {}  # ejemplo: {"usuario1": "Python"}
        self.resultados = {op: 0 for op in opciones}
        self.estado = "activa"
        self.timestamp_inicio = datetime.now()
        self.duracion = timedelta(seconds=duracion_segundos)
        self.tipo = tipo  # simple, multiple...

    def esta_activa(self):
        ahora = datetime.now()
        tiempo_final = self.timestamp_inicio + self.duracion
        return ahora < tiempo_final and self.estado == "activa"

    
