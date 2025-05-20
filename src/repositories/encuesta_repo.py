from abc import ABC, abstractmethod
from src.config import cargar_config

class EncuestaRepository(ABC):
    @abstractmethod
    def guardar_encuesta(self, encuesta_dict):
        pass

    @abstractmethod
    def obtener_encuesta(self, encuesta_id):
        pass


def crear_encuesta_repo():
    config = cargar_config()
    tipo = config.get("base_datos")

    if tipo == "mongo":
        from src.repositories.mongo.encuesta_repo_mongo import EncuestaRepositoryMongo
        return EncuestaRepositoryMongo(config["mongo_uri"])

    elif tipo == "firebase":
        from src.repositories.firebase.encuesta_repo_firebase import EncuestaRepositoryFirebase
        return EncuestaRepositoryFirebase(config["firebase_key"])

    elif tipo == "neo4j":
        from src.repositories.neo4j.encuesta_repo_neo4j import EncuestaRepositoryNeo4j
        return EncuestaRepositoryNeo4j(
            config["neo4j_uri"],
            config["neo4j_user"],
            config["neo4j_password"]
        )

    else:
        raise Exception("Tipo de base de datos no soportado: " + tipo)




