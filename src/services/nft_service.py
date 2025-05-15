import uuid
from datetime import datetime
from repositories.nft_repo import NFTRepository

class NFTService:
    def __init__(self, repo: NFTRepository):
        self.repo = repo

    def generar_token(self, username, poll_id, opcion):
        token_dict = {
            "token_id": str(uuid.uuid4()),
            "owner": username,
            "poll_id": poll_id,
            "option": opcion,
            "issued_at": datetime.now().isoformat()
        }
        self.repo.guardar_token(token_dict)
        return token_dict

    def transferir_token(self, token_id, nuevo_owner):
        self.repo.transferir_token(token_id, nuevo_owner)

    def obtener_tokens_usuario(self, username):
        tokens = self.repo.cargar_todos()
        return [t for t in tokens if t["owner"] == username]

