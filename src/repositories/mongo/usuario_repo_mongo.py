from pymongo import MongoClient
from src.repositories.usuario_repo import UsuarioRepository

class UsuarioRepositoryMongo(UsuarioRepository):
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client["la_ultima"]
        self.usuarios = self.db["usuarios"]

    def buscar_usuario(self, username):
        usuario = self.usuarios.find_one({"username": username})
        if usuario:
            usuario.pop("_id", None)  # elimina el campo _id si existe
        return usuario

    def guardar_usuario(self, usuario_dict):
        self.usuarios.insert_one(usuario_dict)
