from abc import ABC, abstractmethod
from src.config import cargar_config

class EncuestaRepository(ABC):
    @abstractmethod
    def guardar_encuesta(self, encuesta_dict):
        pass

    @abstractmethod
    def obtener_encuesta(self, encuesta_id):
        pass

# Dummy temporal para desarrollo
class DummyEncuestaRepo(EncuestaRepository):
    def _init_(self):
        self.db = {}

    def guardar_encuesta(self, encuesta_dict):
        self.db[encuesta_dict["id"]] = encuesta_dict

    def obtener_encuesta(self, encuesta_id):
        return self.db.get(encuesta_id, None)

def crear_encuesta_repo():
    config = cargar_config()
    tipo = config.get("base_datos")

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





