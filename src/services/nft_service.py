from src.repositories.nft_repo import crear_nft_repo

class NFTService:
    def __init__(self):
        self.repo = crear_nft_repo()

    def generar_token(self, username, encuesta_id, opcion):
        token = {
            "owner": username,
            "encuesta_id": encuesta_id,
            "opcion": opcion
        }
        self.repo.guardar_token(token)

    def obtener_tokens_usuario(self, username):
        return self.repo.obtener_tokens_usuario(username)

    def transferir_token(self, token_id, nuevo_owner):
        self.repo.transferir_token(token_id, nuevo_owner)

