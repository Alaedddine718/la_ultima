from abc import ABC, abstractmethod

class UsuarioRepository(ABC):
    @abstractmethod
    def guardar_usuario(self, usuario_dict):
        pass

    @abstractmethod
    def buscar_usuario(self, username):
        pass

from src.config import cargar_config

def crear_usuario_repo():
    config = cargar_config()
    tipo = config.get("base_datos")

    if tipo == "mongo":
        from src.repositories.mongo.usuario_repo_mongo import UsuarioRepositoryMongo
        return UsuarioRepositoryMongo(config["mongo_uri"])
    
    elif tipo == "firebase":
        from src.repositories.firebase.usuario_repo_firebase import UsuarioRepositoryFirebase
        return UsuarioRepositoryFirebase(config["firebase_key"])
    
    elif tipo == "neo4j":
        from src.repositories.neo4j.usuario_repo_neo4j import UsuarioRepositoryNeo4j
        return UsuarioRepositoryNeo4j(
            config["neo4j_uri"], config["neo4j_user"], config["neo4j_password"]
        )
    
    else:
        raise Exception("Tipo de base de datos no soportado: " + tipo)
