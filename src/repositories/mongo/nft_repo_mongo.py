from pymongo import MongoClient
from src.repositories.nft_repo import NFTRepository

class NFTRepositoryMongo(NFTRepository):
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client["la_ultima"]
        self.tokens = self.db["tokens"]

    def guardar_token(self, token_dict):
        self.tokens.insert_one(token_dict)

    def obtener_tokens_usuario(self, username):
        tokens = list(self.tokens.find({"owner": username}))
        for t in tokens:
            t.pop("_id", None)
        return tokens

    def transferir_token(self, token_id, nuevo_owner):
        self.tokens.update_one({"token_id": token_id}, {"$set": {"owner": nuevo_owner}})
