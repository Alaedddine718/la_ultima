from pymongo import MongoClient
from datetime import datetime, timedelta
from src.repositories.encuesta_repo import EncuestaRepository

class EncuestaRepositoryMongo(EncuestaRepository):
    def _init_(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client["la_ultima"]
        self.encuestas = self.db["encuestas"]

    def guardar_encuesta(self, encuesta_dict):
        self.encuestas.replace_one({"id": encuesta_dict["id"]}, encuesta_dict, upsert=True)

    def obtener_encuesta(self, encuesta_id):
        encuesta = self.encuestas.find_one({"id": encuesta_id})
        if encuesta:
            encuesta.pop("_id", None)
        return encuesta

    def obtener_resultados(self, encuesta_id):
        encuesta = self.obtener_encuesta(encuesta_id)
        if not encuesta:
            return {}
        return encuesta.get("resultados", {})

    def votar(self, encuesta_id, username, opcion):
        encuesta = self.obtener_encuesta(encuesta_id)
        if not encuesta:
            raise Exception("Encuesta no encontrada.")

        if "resultados" not in encuesta:
            encuesta["resultados"] = {}

        if opcion not in encuesta["resultados"]:
            encuesta["resultados"][opcion] = 0

        encuesta["resultados"][opcion] += 1
        self.guardar_encuesta(encuesta)

    def obtener_encuestas_activas(self):
        ahora = datetime.now()
        activas = []
        for encuesta in self.encuestas.find():
            inicio = datetime.fromisoformat(encuesta["inicio"])
            duracion = int(encuesta["duracion"])
            if ahora < inicio + timedelta(seconds=duracion):
                encuesta.pop("_id", None)
                activas.append(encuesta)
        return activas
