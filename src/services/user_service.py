import bcrypt
import uuid
from src.repositories.usuario_repo import UsuarioRepository

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

    def login(self, username, password):
        usuario = self.repo.buscar_usuario(username)
        if not usuario:
            raise Exception("Usuario no encontrado.")
        if not bcrypt.checkpw(password.encode(), usuario["password_hash"].encode()):
            raise Exception("Contraseña incorrecta.")
        token_sesion = str(uuid.uuid4())
        self.sesiones[username] = token_sesion
        return token_sesion

    def verificar_login(self, username, token_sesion):
        return self.sesiones.get(username) == token_sesion

