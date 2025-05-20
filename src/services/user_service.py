import bcrypt
import uuid

class UserService:
    def _init_(self, repo):
        self.repo = repo
        self.sesiones = {}

    def registrar(self, username, password):
        if self.repo.buscar_usuario(username):
            raise Exception("El usuario ya existe.")
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.repo.guardar_usuario({
            "username": username,
            "password_hash": hashed.decode(),
            "tokens": []
        })
        return "Usuario registrado correctamente."

    def login(self, username, password):
        usuario = self.repo.buscar_usuario(username)
        if not usuario:
            raise Exception("Usuario no encontrado.")
        if not bcrypt.checkpw(password.encode(), usuario["password_hash"].encode()):
            raise Exception("Contraseña incorrecta.")
        token = str(uuid.uuid4())
        self.sesiones[username] = token
        return f"Inicio de sesión correcto. Token: {token}"

    def verificar_login(self, username, token):
        return self.sesiones.get(username) == token
