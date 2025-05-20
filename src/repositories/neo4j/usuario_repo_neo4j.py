from src.repositories.usuario_repo import UsuarioRepository

class UsuarioRepositoryNeo4j(UsuarioRepository):
    def __init__(self, uri, user, password):
        self.usuarios = {}  # Simulación local

    def guardar_usuario(self, usuario_dict):
        self.usuarios[usuario_dict["username"]] = usuario_dict

    def buscar_usuario(self, username):
        return self.usuarios.get(username)


