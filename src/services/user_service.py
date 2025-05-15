import bcrypt
import uuid
from repositories.usuario_repo import UsuarioRepository

class UserService:
    def __init__(self, repo: UsuarioRepository):
        self.repo = repo
        self.sesiones = {}

    def registrar(self, username, password):
        if self.repo.buscar_usuario(username):
            raise Exception("Usuario ya existe.")
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        usuario_dict = {
            "username": username,
            "password_hash": hashed.decode(),
            "tokens": []
        }
        self.repo.guardar_usuario(usuario_dict)

   
