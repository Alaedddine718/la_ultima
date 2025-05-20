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
