from src.repositories.nft_repo import NFTRepository

class NFTRepositoryFirebase(NFTRepository):
    def __init__(self, firebase_key):
        self.tokens = {}  # Simulación simple para pruebas

    def guardar_token(self, token_dict):
        self.tokens[token_dict["id"]] = token_dict

    def obtener_tokens_usuario(self, username):
        return [token for token in self.tokens.values() if token["owner"] == username]

    def transferir_token(self, token_id, nuevo_owner):
        if token_id in self.tokens:
            self.tokens[token_id]["owner"] = nuevo_owner
