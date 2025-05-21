import uuid
from datetime import datetime, timedelta

class PollService:
    def __init__(self, encuesta_repo):
        self.encuesta_repo = encuesta_repo
        self.encuestas_activas = {}  # Memoria temporal para encuestas activas

    def crear_encuesta(self, pregunta, opciones, creador, duracion):
        encuesta_id = str(uuid.uuid4())
        encuesta = {
            "id": encuesta_id,
            "pregunta": pregunta,
            "opciones": opciones,
            "creador": creador,
            "duracion": duracion,
            "estado": "activa",
            "inicio": datetime.now().isoformat()
        }
        self.encuesta_repo.guardar_encuesta(encuesta)
        self.encuestas_activas[encuesta_id] = encuesta
        return encuesta_id

    def votar(self, encuesta_id, username, opcion):
        self.encuesta_repo.votar(encuesta_id, username, opcion)

    def obtener_resultados(self, encuesta_id):
        return self.encuesta_repo.obtener_resultados(encuesta_id)

    def obtener_encuestas_activas(self):
        return list(self.encuestas_activas.values())



