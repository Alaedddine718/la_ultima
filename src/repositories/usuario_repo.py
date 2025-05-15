import json
import os

class UsuarioRepository:
    def __init__(self, ruta_archivo="data/usuarios.json"):
        self.ruta = ruta_archivo
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(self.ruta):
            with open(self.ruta, "w") as f:
                json.dump([], f)

    def guardar_usuario(self, usuario_dict):
        usuarios = self.cargar_todos()
        usuarios.append(usuario_dict)
        with open(self.ruta, "w") as f:
            json.dump(usuarios, f, indent=4)

    def buscar_usuario(self, username):
        usuarios = self.cargar_todos()
        for u in usuarios:
            if u["username"] == username:
                return u
        return None

    def cargar_todos(self):
        with open(self.ruta, "r") as f:
            return json.load(f)
