from abc import ABC, abstractmethod
from src.config import cargar_config

class EncuestaRepository(ABC):
    @abstractmethod
    def guardar_encuesta(self, encuesta_dict):
        pass

    @abstractmethod
    def obtener_encuesta(self, encuesta_id):
        pass

    @abstractmethod
    def obtener_resultados(self, encuesta_id):
        pass

    @abstractmethod
    def votar(self, encuesta_id, username, opcion):
        pass

    @abstractmethod
    def obtener_encuestas_activas(self):
        pass


class DummyEncuestaRepo(EncuestaRepository):
    def __init__(self):
        self.encuestas = {}

    def guardar_encuesta(self, encuesta_dict):
        self.encuestas[encuesta_dict["id"]] = encuesta_dict

    def obtener_encuesta(self, encuesta_id):
        return self.encuestas.get(encuesta_id)

    def obtener_resultados(self, encuesta_id):
        encuesta = self.encuestas.get(encuesta_id)
        if not encuesta:
            return "Encuesta no encontrada."
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
        return list(self.encuestas.values())


def crear_encuesta_repo():
    config = cargar_config()
    tipo = config.get("base_datos", "dummy")

    if tipo == "dummy":
        return DummyEncuestaRepo()
    
    elif tipo == "mongo":
        from src.repositories.mongo.encuesta_repo_mongo import EncuestaRepositoryMongo
        return EncuestaRepositoryMongo(config["mongo_uri"])
    
    elif tipo == "firebase":
        from src.repositories.firebase.encuesta_repo_firebase import EncuestaRepositoryFirebase
        return EncuestaRepositoryFirebase(config["firebase_key"])
    
    elif tipo == "neo4j":
        from src.repositories.neo4j.encuesta_repo_neo4j import EncuestaRepositoryNeo4j
        return EncuestaRepositoryNeo4j(
            config["neo4j_uri"], config["neo4j_user"], config["neo4j_password"]
        )
    
    else:
        raise Exception("Tipo de base de datos no soportado: " + str(tipo))




