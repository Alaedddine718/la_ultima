import bcrypt
import uuid

class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo
        self.sesiones = {}  # Para manejar sesiones locales

    def registrar_usuario(self, username, password):
        if self.user_repo.buscar_usuario(username):
            return False  # Ya existe
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        usuario = {
            "username": username,
            "password_hash": hashed.decode(),
            "tokens": []
        }
        self.user_repo.guardar_usuario(usuario)
        return True

    def verificar_credenciales(self, username, password):
        usuario = self.user_repo.buscar_usuario(username)
        if not usuario:
            return False
        return bcrypt.checkpw(password.encode(), usuario["password_hash"].encode())

    def obtener_usuario(self, username):
        return self.user_repo.buscar_usuario(username)

