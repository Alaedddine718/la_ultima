from neo4j import GraphDatabase
from src.repositories.usuario_repo import UsuarioRepository

class UsuarioRepositoryNeo4j(UsuarioRepository):
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def buscar_usuario(self, username):
        query = "MATCH (u:Usuario {username: $username}) RETURN u LIMIT 1"
        with self.driver.session() as session:
            result = session.run(query, username=username)
            record = result.single()
            if record:
                return record["u"]
        return None

    def guardar_usuario(self, usuario_dict):
        query = "CREATE (u:Usuario {username: $username, password_hash: $password_hash, tokens: []})"
        with self.driver.session() as session:
            session.run(query, username=usuario_dict["username"], password_hash=usuario_dict["password_hash"])
