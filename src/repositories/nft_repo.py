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

class NFTRepositoryDummy(NFTRepository):
    def _init_(self):
        self.tokens = []

    def guardar_token(self, token_dict):
        self.tokens.append(token_dict)

    def obtener_tokens_usuario(self, username):
        return [t for t in self.tokens if t["owner"] == username]

    def transferir_token(self, token_id, nuevo_owner):
        for t in self.tokens:
            if t["id"] == token_id:
                t["owner"] = nuevo_owner
                return

def crear_nft_repo():
    config = cargar_config()
    tipo = config.get("base_datos")
    if tipo == "dummy":
        return NFTRepositoryDummy()
    raise Exception("Tipo de base de datos no soportado: " + tipo)



