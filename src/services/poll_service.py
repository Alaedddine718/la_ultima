import uuid
from datetime import datetime, timedelta

class PollService:
    def _init_(self, encuesta_repo):
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
            "inicio": datetime.now().isoformat(),
            "votos": {}
        }
        self.encuesta_repo.guardar_encuesta(encuesta)
        self.encuestas_activas[encuesta_id] = encuesta
        return encuesta_id

    def votar(self, encuesta_id, username, opcion):
        encuesta = self.encuestas_activas.get(encuesta_id)
        if not encuesta:
            raise Exception("Encuesta no activa o no encontrada.")

        if encuesta["estado"] != "activa":
            raise Exception("La encuesta está cerrada.")

        self.encuesta_repo.votar(encuesta_id, username, opcion)

    def obtener_resultados(self, encuesta_id):
        return self.encuesta_repo.obtener_resultados(encuesta_id)

    def obtener_encuestas_activas(self):
        return list(self.encuestas_activas.values())



