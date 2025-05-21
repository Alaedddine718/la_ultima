from abc import ABC, abstractmethod
from src.config import cargar_config

class UsuarioRepository(ABC):
    @abstractmethod
    def guardar_usuario(self, usuario_dict):
        pass

    @abstractmethod
    def buscar_usuario(self, username):
        pass

class UsuarioRepositoryDummy(UsuarioRepository):
    def _init_(self):  # ← ← ← Corregido aquí
        self.usuarios = {}

    def guardar_usuario(self, usuario_dict):
        self.usuarios[usuario_dict["username"]] = usuario_dict

    def buscar_usuario(self, username):
        return self.usuarios.get(username)

def crear_usuario_repo():
    config = cargar_config()
    tipo = config.get("base_datos", "dummy")

    if tipo == "mongo":
        from src.repositories.mongo.usuario_repo_mongo import UsuarioRepositoryMongo
        return UsuarioRepositoryMongo(config["mongo_uri"])

    elif tipo == "firebase":
        from src.repositories.firebase.usuario_repo_firebase import UsuarioRepositoryFirebase
        return UsuarioRepositoryFirebase(config["firebase_key"])

    elif tipo == "neo4j":
        from src.repositories.neo4j.usuario_repo_neo4j import UsuarioRepositoryNeo4j
        return UsuarioRepositoryNeo4j(
            config["neo4j_uri"],
            config["neo4j_user"],
            config["neo4j_password"]
        )

    else:
        return UsuarioRepositoryDummy()


