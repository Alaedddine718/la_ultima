from abc import ABC, abstractmethod
from src.config import cargar_config

class NFTRepository(ABC):
    @abstractmethod
    def guardar_token(self, token_dict):
        pass

    @abstractmethod
    def obtener_tokens_usuario(self, username):
        pass

    @abstractmethod
    def transferir_token(self, token_id, nuevo_owner):
        pass

def crear_nft_repo():
    config = cargar_config()
    tipo = config.get("base_datos")

    if tipo == "mongo":
        from src.repositories.mongo.nft_repo_mongo import NFTRepositoryMongo
        return NFTRepositoryMongo(config["mongo_uri"])

    elif tipo == "firebase":
        from src.repositories.firebase.nft_repo_firebase import NFTRepositoryFirebase
        return NFTRepositoryFirebase(config["firebase_key"])

    elif tipo == "neo4j":
        from src.repositories.neo4j.nft_repo_neo4j import NFTRepositoryNeo4j
        return NFTRepositoryNeo4j(
            config["neo4j_uri"],
            config["neo4j_user"],
            config["neo4j_password"]
        )

    else:
        raise Exception("Tipo de base de datos no soportado: " + tipo)


