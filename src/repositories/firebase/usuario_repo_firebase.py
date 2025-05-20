import firebase_admin
from firebase_admin import credentials, firestore
from src.repositories.usuario_repo import UsuarioRepository

class UsuarioRepositoryFirebase(UsuarioRepository):
    def __init__(self, key_path):
        if not firebase_admin._apps:
            cred = credentials.Certificate(key_path)
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.usuarios = self.db.collection("usuarios")

    def buscar_usuario(self, username):
        doc = self.usuarios.document(username).get()
        if doc.exists:
            return doc.to_dict()
        return None

    def guardar_usuario(self, usuario_dict):
        self.usuarios.document(usuario_dict["username"]).set(usuario_dict)
