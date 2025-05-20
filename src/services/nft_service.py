class NFTService:
    def __init__(self, nft_repo, config):
        self.nft_repo = nft_repo
        self.config = config

    def generar_token(self, username, poll_id, opcion):
        token = {
            "username": username,
            "poll_id": poll_id,
            "opcion": opcion
        }
        self.nft_repo.guardar_token(token)

    def obtener_tokens_usuario(self, username):
        return self.nft_repo.obtener_tokens_usuario(username)

    def transferir_token(self, token_id, nuevo_owner):
        self.nft_repo.transferir_token(token_id, nuevo_owner)





