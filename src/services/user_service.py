class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def registrar_usuario(self, username, password):
        return self.user_repo.registrar(username, password)

    def verificar_credenciales(self, username, password):
        return self.user_repo.verificar_credenciales(username, password)

    def obtener_usuario(self, username):
        return self.user_repo.obtener_usuario(username)

