from src.repositories.encuesta_repo import EncuestaRepository
from datetime import datetime, timedelta

class EncuestaRepositoryDummy(EncuestaRepository):
    def __init__(self):
        self.encuestas = {}

    def guardar_encuesta(self, encuesta_dict):
        encuesta_id = encuesta_dict.get("id")
        if not encuesta_id:
            raise ValueError("La encuesta debe tener un ID.")
        encuesta_dict["resultados"] = {}
        self.encuestas[encuesta_id] = encuesta_dict

    def obtener_encuesta(self, encuesta_id):
        return self.encuestas.get(encuesta_id)

    def obtener_resultados(self, encuesta_id):
        encuesta = self.encuestas.get(encuesta_id)
        if not encuesta:
            raise Exception("Encuesta no encontrada.")
        return encuesta.get("resultados", {})

    def votar(self, encuesta_id, username, opcion):
        encuesta = self.encuestas.get(encuesta_id)
        if not encuesta:
            raise Exception("Encuesta no encontrada.")
        if "resultados" not in encuesta:
            encuesta["resultados"] = {}
        if opcion not in encuesta["resultados"]:
            encuesta["resultados"][opcion] = 0
        encuesta["resultados"][opcion] += 1

    def obtener_encuestas_activas(self):
        activas = []
        ahora = datetime.now()
        for encuesta in self.encuestas.values():
            inicio = datetime.fromisoformat(encuesta["inicio"])
            duracion = int(encuesta["duracion"])
            if ahora < inicio + timedelta(seconds=duracion):
                activas.append(encuesta)
        return activas