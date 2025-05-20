from abc import ABC, abstractmethod

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

