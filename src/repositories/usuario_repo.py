from abc import ABC, abstractmethod

class UsuarioRepository(ABC):
    @abstractmethod
    def guardar_usuario(self, usuario_dict):
        pass

    @abstractmethod
    def buscar_usuario(self, username):
        pass

