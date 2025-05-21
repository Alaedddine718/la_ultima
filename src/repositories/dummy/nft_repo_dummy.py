from src.repositories.nft_repo import NFTRepository

class NFTRepositoryDummy(NFTRepository):
    def _init_(self):
        self.tokens = {}
        self.next_id = 1

    def guardar_token(self, token_dict):
        token_id = str(self.next_id)
        token_dict["id"] = token_id
        self.tokens[token_id] = token_dict
        self.next_id += 1
        return token_id

    def obtener_tokens_usuario(self, username):
        return [token for token in self.tokens.values() if token["owner"] == username]

    def transferir_token(self, token_id, nuevo_owner):
        if token_id in self.tokens:
            self.tokens[token_id]["owner"] = nuevo_owner
        else:
            raise Exception("Token no encontrado.")