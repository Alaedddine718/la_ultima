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
    def votar(self, username, opcion):
        if not self.esta_activa():
            raise Exception("La encuesta ya está cerrada.")
        if username in self.votos:
            raise Exception("Este usuario ya votó.")
        if opcion not in self.opciones:
            raise Exception("Opción no válida.")
        self.votos[username] = opcion
        self.resultados[opcion] += 1

    def cerrar(self):
        self.estado = "cerrada"

    def get_resultados(self):
        total = sum(self.resultados.values())
        return {
            opcion: f"{(count / total) * 100:.1f}%" if total > 0 else "0%"
            for opcion, count in self.resultados.items()
        }

    
