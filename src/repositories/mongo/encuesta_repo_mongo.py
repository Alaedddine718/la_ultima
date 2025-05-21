from pymongo import MongoClient
from src.repositories.encuesta_repo import EncuestaRepository

class EncuestaRepositoryMongo(EncuestaRepository):
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client["la_ultima"]
        self.encuestas = self.db["encuestas"]

    def guardar_encuesta(self, encuesta_dict):
        self.encuestas.replace_one({"id": encuesta_dict["id"]}, encuesta_dict, upsert=True)

    def obtener_encuesta(self, encuesta_id):
        return self.encuestas.find_one({"id": encuesta_id})

    def obtener_resultados(self, encuesta_id):
        encuesta = self.obtener_encuesta(encuesta_id)
        if not encuesta:
            raise Exception("Encuesta no encontrada.")
        return encuesta.get("resultados", {})

    def votar(self, encuesta_id, username, opcion):
        encuesta = self.obtener_encuesta(encuesta_id)
        if not encuesta:
            raise Exception("Encuesta no encontrada.")
        resultados = encuesta.get("resultados", {})
        resultados[opcion] = resultados.get(opcion, 0) + 1
        encuesta["resultados"] = resultados
        self.guardar_encuesta(encuesta)

    def obtener_encuestas_activas(self):
        return list(self.encuestas.find({"estado": "activa"}))
