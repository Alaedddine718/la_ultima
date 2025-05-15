from models.encuesta import Encuesta
from repositories.encuesta_repo import EncuestaRepository
from datetime import datetime

class PollService:
    def __init__(self, repo: EncuestaRepository):
        self.repo = repo
        self.encuestas_activas = {}

    def crear_encuesta(self, pregunta, opciones, duracion_segundos, tipo="simple"):
        encuesta = Encuesta(pregunta, opciones, duracion_segundos, tipo)
        self.encuestas_activas[encuesta.id] = encuesta
        self.repo.guardar_encuesta(self._a_dict(encuesta))
        return encuesta.id

    def votar(self, poll_id, username, opcion):
        self._verificar_tiempos()
        encuesta = self.encuestas_activas.get(poll_id)
        if not encuesta:
            raise Exception("Encuesta no encontrada o ya cerrada.")
        encuesta.votar(username, opcion)
        return encuesta.resultados

   
